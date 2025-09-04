from __future__ import annotations

import asyncio
import os
import struct
import contextlib
import json

from hashlib import md5
from pathlib import Path

from client.constants import CONFIG_PROTOCOL_HEADER_EXCEPT_FIRST_LEN, ADVERTISING_ID, MD5_SECRET
from client.events import EventManager, Event
from client.protobuf import dr2_login_pb_pb2 as login_pb, dr2_logic_pb_pb2 as logic_pb
from client.net.tcpclient import TCPClient, Frame
from client.config import ClientConfig, AccountConfig, CONFIG_DIR


class IHNetClient:
    def __init__(self):
        _client_src_dir = os.path.dirname(os.path.abspath(__file__))
        self.event_manager = EventManager(os.path.join(_client_src_dir, "assets", "events.json"))
        self.account_config = AccountConfig.get()
        self.client_config = ClientConfig.get()
        self.tcp_client = TCPClient(self.client_config)

        self.sid = 0
        self.echo_count = 1
        self._waiters: dict[tuple[int, int], asyncio.Future[bytes]] = {}
        self._streams: dict[tuple[int, int], asyncio.Queue[Frame]] = {}
        self._router_task: asyncio.Task | None = None
        self._router_started = asyncio.Event()

    @classmethod
    async def create(cls, host: str, port: int, timeout: float = 10.0) -> IHNetClient:
        self = cls()

        await self.connect(host, port)
        self._router_task = asyncio.create_task(self._router_loop())
        await self._router_started.wait()

        return self

    @classmethod
    async def create_from_config(cls) -> IHNetClient:
        self = cls()

        await self.connect(self.client_config.gateway_host, self.client_config.gateway_port)
        self._router_task = asyncio.create_task(self._router_loop())
        await self._router_started.wait()

        return self

    def get_account(self) -> AccountConfig:
        return self.account_config

    def set_account(self, account: AccountConfig):
        self.account_config = account

    async def connect(self, host: str, port: int):
        await self.tcp_client.connect(host, port, self.client_config.conn_timeout)

    async def disconnect(self):
        if self._router_task is not None:
            self._router_task.cancel()

            with contextlib.suppress(asyncio.CancelledError):
                await self._router_task

            self._router_task = None

        for fut in self._waiters.values():
            if not fut.done():
                fut.set_exception(ConnectionError("Disconnected"))
        self._waiters.clear()

        await self.tcp_client.disconnect()

    def _build_packet(self, group: int, cmd: int, sid: int, payload: bytes) -> bytes:
        after_len = CONFIG_PROTOCOL_HEADER_EXCEPT_FIRST_LEN + len(payload)
        return struct.pack(">HBBH", after_len, group & 0xFF, cmd & 0xFF, sid & 0xFFFF) + payload

    async def _router_loop(self):
        self._router_started.set()
        while True:
            frame = await self.tcp_client.message_queue.get()
            key_waiter = (frame.cmd_type, frame.cmd_id)
            fut = self._waiters.pop(key_waiter, None)

            if fut is not None and not fut.done():
                fut.set_result(frame.payload)
                continue

            queue = self._streams.get(key_waiter)
            if queue is not None:
                await queue.put(frame)
                continue

            raise RuntimeError(f"Unroutable frame: cmd_type={frame.cmd_type} cmd_id={frame.cmd_id}")

    async def submit(self, event: Event, payload: bytes, buffer_size: int = -1) -> bytes:
        packet = self._build_packet(event.cmd_group, event.cmd_type, self.sid, payload)
        loop = asyncio.get_running_loop()
        key = (event.cmd_group, event.cmd_type)
        fut: asyncio.Future[bytes] = loop.create_future()

        self._waiters[key] = fut

        await self.tcp_client.send(packet)

        try:
            return await asyncio.wait_for(fut, timeout=self.client_config.conn_timeout)
        finally:
            self._waiters.pop(key, None)

    # commands
    async def echo(self) -> login_pb.pbrsp_echo:
        _sid = self.sid
        self.sid = 0

        event = self.event_manager.get_event("EVENT_CMD_1_1")
        payload = login_pb.pbreq_echo(echo=self.echo_count)

        rsp_data = await self.submit(event, payload.SerializeToString())
        rsp = login_pb.pbrsp_echo()
        rsp.ParseFromString(rsp_data)

        self.echo_count += 1
        self.sid = _sid

        return rsp

    async def salt(self) -> login_pb.pbrsp_salt:
        event = self.event_manager.get_event("EVENT_CMD_2_2")
        payload = login_pb.pbreq_salt(account=self.account_config.account)

        rsp_data = await self.submit(event, payload.SerializeToString())
        rsp = login_pb.pbrsp_salt()
        rsp.ParseFromString(rsp_data)

        return rsp

    async def reg(self) -> login_pb.pbrsp_reg:
        event = self.event_manager.get_event("EVENT_CMD_2_1")
        payload = login_pb.pbreq_reg(
            rdid=ADVERTISING_ID,
        )

        rsp_data = await self.submit(event, payload.SerializeToString())
        rsp = login_pb.pbrsp_reg()
        rsp.ParseFromString(rsp_data)

        return rsp

    async def login(self, salt: str) -> login_pb.pbrsp_login:
        event = self.event_manager.get_event("EVENT_CMD_2_3")
        password = md5(self.account_config.password.encode("utf-8")).hexdigest()
        password_md5 = md5((salt + MD5_SECRET + password).encode("utf-8")).hexdigest()
        self.sid = 0

        payload = login_pb.pbreq_login(
            checksum=password_md5,
            idfa=ADVERTISING_ID,
            keychain="",
            idfv=""
        )

        rsp_data = await self.submit(event, payload.SerializeToString())
        rsp = login_pb.pbrsp_login()
        rsp.ParseFromString(rsp_data)

        self.sid = rsp.sid

        return rsp

    def _get_env_info(self) -> dict:
        env_data = Path(os.path.join(CONFIG_DIR, "env.json")).read_text()
        env_info = json.loads(env_data)

        return env_info

    async def auth(self, uid: int, session: str) -> logic_pb.pbrsp_auth:
        env_info = self._get_env_info()
        tracking_ids = "{}"  # don't track me

        event = self.event_manager.get_event("EVENT_CMD_3_1")
        payload = logic_pb.pbreq_auth(
            uid=uid,
            session=session,
            env=json.dumps(env_info),
            ids=tracking_ids,
            support_zip=1,
        )

        rsp_data = await self.submit(event, payload.SerializeToString())
        rsp = logic_pb.pbrsp_auth()
        rsp.ParseFromString(rsp_data)

        return rsp
