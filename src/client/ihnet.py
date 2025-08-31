from __future__ import annotations

import asyncio
import os
import struct
import contextlib

from client.constants import CONFIG_PROTOCOL_HEADER_EXCEPT_FIRST_LEN
from client.events import EventManager, Event
from client.protobuf import dr2_login_pb_pb2 as login_pb
from client.net.tcpclient import TCPClient, Frame
from client.config import ClientConfig, AccountConfig


class IHNetClient:
    def __init__(self):
        _client_src_dir = os.path.dirname(os.path.abspath(__file__))
        self.event_manager = EventManager(os.path.join(_client_src_dir, "assets", "events.json"))
        self.tcp_client = TCPClient()
        self.account_config = AccountConfig.get()
        self.client_config = ClientConfig.get()

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
