from __future__ import annotations

import asyncio
import os
import struct
import contextlib
import json

from hashlib import md5
from pathlib import Path
from packaging import version
from enum import Enum

from google.protobuf.json_format import MessageToJson

from client.constants import (
    CONFIG_PROTOCOL_HEADER_EXCEPT_FIRST_LEN,
    ADVERTISING_ID,
    MD5_SECRET,
    ROOT_DIR,
    PACKAGE_NAME
)
from client.events import EventManager, Event
from client.protobuf import dr2_login_pb_pb2 as login_pb, dr2_logic_pb_pb2 as logic_pb
from client.protobuf import dr2_comm_pb_pb2 as comm_pb
from client.net.tcpclient import TCPClient, Frame
from client.config import ClientConfig, AccountConfig, CONFIG_DIR, FarmConfig
from client.models.player import LocalPlayer
from client.models.mail import MailOpType, IHMail
from client.models.bag import IHBag
from client.updater import Updater, UpdateType
from client.utils import Utils


class IHNetError(Exception):
    pass


class NetClientStatus(Enum):
    UPDATE_NOT_READY = 0
    CONNECTED = 1


class IHNetClient:
    def __init__(self):
        _client_src_dir = os.path.dirname(os.path.abspath(__file__))
        self.event_manager = EventManager(os.path.join(_client_src_dir, "assets", "events.json"))
        self.account_config = AccountConfig.get()
        self.client_config = ClientConfig.get()
        self.farm_config = FarmConfig.get()
        self.tcp_client = TCPClient(self.client_config)
        self.updater = Updater(self.client_config)

        self.sid = 0
        self.echo_count = 1
        self.local_player: LocalPlayer = LocalPlayer()
        self._waiters: dict[tuple[int, int], asyncio.Future[bytes]] = {}
        self._streams: dict[tuple[int, int], asyncio.Queue[Frame]] = {}
        self._router_task: asyncio.Task | None = None
        self._heartbeat_task: asyncio.Task | None = None
        self._farming_task: asyncio.Task | None = None
        self._router_started = asyncio.Event()
        self._update_not_ready = asyncio.Event()
        self._initialized = asyncio.Event()
        self._push_event_handlers = {
            event_name.cmd: getattr(self, f"_on_{event_name.cmd.lower()}", None)
            for event_name in self.event_manager.push_events
        }

    def check_account(self) -> bool:
        if self.account_config.account == "" or self.account_config.password == "":
            return False
        return True

    async def check_update(self) -> bool:
        await self.updater.ensure_resources_dir()

        print("[IHNetClient] Checking for updates...")
        up_rsp = await self.up()
        if up_rsp.status != 0:
            raise IHNetError(f"Failed to check version: status={up_rsp.status}")

        if up_rsp.vsn != self.client_config.version:
            print(f"[IHNetClient] New version available: {up_rsp.vsn} (current: {self.client_config.version})")

            new_version = version.parse(up_rsp.vsn)
            result = await self.updater.check_for_update(new_version)
            if result != UpdateType.NONE:
                print(f"[IHNetClient] Installing update to version {new_version}...")

                if result == UpdateType.MAJOR:
                    await self.updater.install_major_update(new_version)
                elif result == UpdateType.MINOR:
                    await self.updater.install_minor_update(new_version)
                else:
                    await self.updater.install_patch_update(new_version)

                self.client_config.version = str(new_version)
                self.client_config.save()

                print(f"[IHNetClient] Update to version {new_version} installed successfully.")

                return True
            else:
                self._update_not_ready.set()
        else:
            print(f"[IHNetClient] Client is up-to-date (version: {self.client_config.version})")
        return False

    async def claim_all_mail(self) -> list[IHMail]:
        mails = self.local_player.get_mails()
        claimed_mails = []

        for mail_item in mails:
            if mail_item.flag == 0 and mail_item.affix is not None:
                rsp = await self.op_mail(mail_item.mail_id, MailOpType.CLAIM)
                if rsp.status == 0:
                    claimed_mails.append(mail_item)

        return claimed_mails

    async def claim_autobattle_rewards(self) -> IHBag:
        print("[IHNetClient] Claiming autobattle rewards...")

        rsp = await self.hook_reward(1)
        if rsp.status != 0:
            raise IHNetError(f"Failed to claim autobattle rewards: status={rsp.status}")

        bag = IHBag.from_pb(rsp.reward)

        print(f"[IHNetClient] Claimed autobattle rewards: {bag}")

        await asyncio.sleep(self.farm_config.autobattle_interval)

        return bag

    async def init(self, no_login: bool = False) -> IHNetClient | NetClientStatus:
        if not self.tcp_client.is_connected():
            await self.connect(self.client_config.gateway_host, self.client_config.gateway_port)
            await self.launch_router()

        if self._heartbeat_task is None:
            self._heartbeat_task = asyncio.create_task(self._heartbeat_loop())

        if no_login:
            return NetClientStatus.CONNECTED

        if not self.check_account():
            print("[IHNetClient] No account configured, please register or set account first.")

            self.account_config.account = input("[IHNetClient] Account Email: ").strip()
            self.account_config.password = input("[IHNetClient] Account Password: ").strip()
            self.account_config.save()
            if not self.check_account():
                raise IHNetError("Account details are incomplete.")

            print("[IHNetClient] Account details saved.")

        print("[IHNetClient] Logging in...")
        salt_rsp = await self.salt()
        if salt_rsp.status != 0:
            raise IHNetError(f"Failed to get salt: status={salt_rsp.status}")

        self.local_player.set_uid(salt_rsp.uid)
        acct_salt = salt_rsp.salt

        login_rsp = await self.login(acct_salt)
        if login_rsp.status != 0:
            raise IHNetError(f"Failed to login: status={login_rsp.status}")

        self.local_player.set_session(login_rsp.session)
        self.local_player.set_sid(login_rsp.sid)

        auth_rsp = await self.auth(self.local_player.get_uid(), self.local_player.get_session())
        if auth_rsp.status != 0:
            raise IHNetError(f"Failed to authenticate: status={auth_rsp.status}")

        print("[IHNetClient] Logged in.")

        while await self.check_update():
            pass

        if self._update_not_ready.is_set():
            return NetClientStatus.UPDATE_NOT_READY

        print("[IHNetClient] Syncing game state...")

        sync_rsp = await self.sync()
        if sync_rsp.status != 0:
            raise IHNetError(f"Failed to sync: status={sync_rsp.status}")

        if self.client_config.debug:
            json_str = MessageToJson(sync_rsp)
            debug_path = os.path.join(ROOT_DIR, "debug")

            os.makedirs(debug_path, exist_ok=True)
            Path(os.path.join(debug_path, "sync.json")).write_text(json_str)

            print(f"[IHNetClient] Sync response saved to {os.path.join(debug_path, 'sync.json')}")

        self.local_player.set_player_from_sync(sync_rsp)
        self.local_player.set_bag_from_sync(sync_rsp)
        self.local_player.set_mails_from_sync(sync_rsp)

        print("[IHNetClient] Game state synced.")
        print("[IHNetClient] Checking mail...")

        mails = await self.claim_all_mail()
        if len(mails) > 0:
            print(f"[IHNetClient] Claimed {len(mails)} mails:")
            for mail in mails:
                print(f"[IHNetClient]   {mail}")
        else:
            print("[IHNetClient] No new mail.")

        self._initialized.set()

        return self

    async def _farming_loop(self):
        print("[IHNetClient] Starting farming loop...")
        print(f"[IHNetClient] Autobattle interval: {self.farm_config.get_autobattle_interval_str()}")

        while True:
            try:
                await self.claim_autobattle_rewards()
            except Exception as e:
                print(f"[IHNetClient] Farming loop error: {e}")
            await asyncio.sleep(5)

    async def run_forever(self):
        if not self._initialized.is_set():
            raise IHNetError("Client not initialized. Call init() first.")

        if self._farming_task is None:
            self._farming_task = asyncio.create_task(self._farming_loop())

        while True:
            try:
                await asyncio.sleep(1)
            except asyncio.CancelledError:
                break

    async def launch_router(self):
        if self._router_task is None:
            self._router_task = asyncio.create_task(self._router_loop())
            await self._router_started.wait()

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

        # save configs
        self.account_config.save()
        self.client_config.save()

    def _build_packet(self, group: int, cmd: int, sid: int, payload: bytes) -> bytes:
        after_len = CONFIG_PROTOCOL_HEADER_EXCEPT_FIRST_LEN + len(payload)
        return struct.pack(">HBBH", after_len, group & 0xFF, cmd & 0xFF, sid & 0xFFFF) + payload

    # mail push event
    async def _on_event_cmd_5_0(self, frame: Frame):
        pb_mail_obj = comm_pb.pb_mail()
        pb_mail_obj.ParseFromString(frame.payload)

        mail = IHMail.from_pb(pb_mail_obj)

        if mail is None:
            print(f"[IHNetClient] Received unknown mail. ID: {pb_mail_obj.id}")
            return

        print(f"[IHNetClient] New mail received: {mail}")

        self.local_player.add_mail(mail)

        if mail.affix is not None:
            await self.op_mail(mail.mail_id, MailOpType.CLAIM)
            print(f"[IHNetClient] Mail {mail.mail_id} rewards claimed.")

    async def _handle_push_event(self, frame: Frame):
        handler = self._push_event_handlers.get(Utils.get_cmd_name(frame.cmd_type, frame.cmd_id), None)
        if handler is not None:
            await handler(frame)
        else:
            if self.client_config.debug:
                print(f"[IHNetClient] Unhandled push event: cmd_type={frame.cmd_type} cmd_id={frame.cmd_id}")

    async def _heartbeat_loop(self):
        heartbeat_data = 12344321
        heartbeat_interval = 60  # seconds

        while True:
            try:
                await self.echo(heartbeat_data)
            except Exception as e:
                print(f"[IHNetClient] Heartbeat failed: {e}")
                await self.disconnect()
                break
            await asyncio.sleep(heartbeat_interval)

    async def _router_loop(self):
        self._router_started.set()
        while True:
            frame = await self.tcp_client.message_queue.get()
            key_waiter = (frame.cmd_type, frame.cmd_id)

            if Utils.get_cmd_name(frame.cmd_type, frame.cmd_id) in self.event_manager.push_events:
                await self._handle_push_event(frame)

            fut = self._waiters.pop(key_waiter, None)

            if fut is not None and not fut.done():
                fut.set_result(frame.payload)
                continue

            queue = self._streams.get(key_waiter)
            if queue is not None:
                await queue.put(frame)
                continue

            # raise RuntimeError(f"Unroutable frame: cmd_type={frame.cmd_type} cmd_id={frame.cmd_id}")

    async def submit(self, event: Event, payload: bytes) -> bytes:
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
    async def echo(self, echo_count: int = 1) -> login_pb.pbrsp_echo:
        event = self.event_manager.get_event("EVENT_CMD_1_1")
        payload = login_pb.pbreq_echo(echo=echo_count)

        rsp_data = await self.submit(event, payload.SerializeToString())
        rsp = login_pb.pbrsp_echo()
        rsp.ParseFromString(rsp_data)

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
            ids=tracking_ids
        )

        rsp_data = await self.submit(event, payload.SerializeToString())
        rsp = logic_pb.pbrsp_auth()
        rsp.ParseFromString(rsp_data)

        return rsp

    async def up(self) -> logic_pb.pbrsp_up:
        event = self.event_manager.get_event("EVENT_CMD_3_3")
        payload = logic_pb.pbreq_up(
            vsn=self.client_config.version,
            packagename=PACKAGE_NAME
        )

        rsp_data = await self.submit(event, payload.SerializeToString())
        rsp = logic_pb.pbrsp_up()
        rsp.ParseFromString(rsp_data)

        return rsp

    async def sync(self) -> logic_pb.pbrsp_sync:
        event = self.event_manager.get_event("EVENT_CMD_3_2")
        payload = logic_pb.pbreq_sync(
            idfa=ADVERTISING_ID,
            keychain="",
            idfv=""
        )

        rsp_data = await self.submit(event, payload.SerializeToString())
        rsp = logic_pb.pbrsp_sync()
        rsp.ParseFromString(rsp_data)

        return rsp

    async def op_mail(self, mid: int, op_type: MailOpType) -> logic_pb.pbrsp_op_mail:
        event = self.event_manager.get_event("EVENT_CMD_5_1")
        payload = logic_pb.pbreq_op_mail(
            reads=[mid] if op_type == MailOpType.READ else None,
            deletes=[mid] if op_type == MailOpType.DELETE else None,
            affixs=[mid] if op_type == MailOpType.CLAIM else None,
            blocks=[mid] if op_type == MailOpType.BLOCK else None,
        )

        rsp_data = await self.submit(event, payload.SerializeToString())
        rsp = logic_pb.pbrsp_op_mail()
        rsp.ParseFromString(rsp_data)

        return rsp

    async def hook_ask(self) -> logic_pb.pbrsp_hook_ask:
        event = self.event_manager.get_event("EVENT_CMD_9_3")
        payload = logic_pb.pbreq_hook_ask()

        rsp_data = await self.submit(event, payload.SerializeToString())
        rsp = logic_pb.pbrsp_hook_ask()
        rsp.ParseFromString(rsp_data)

        return rsp

    async def hook_reward(self, type: int) -> logic_pb.pbrsp_hook_reward:
        event = self.event_manager.get_event("EVENT_CMD_9_4")
        payload = logic_pb.pbreq_hook_reward(type=type)

        rsp_data = await self.submit(event, payload.SerializeToString())
        rsp = logic_pb.pbrsp_hook_reward()
        rsp.ParseFromString(rsp_data)

        return rsp
