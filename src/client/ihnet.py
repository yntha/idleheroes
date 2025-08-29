import asyncio
import os
import struct

from client.constants import CONFIG_PROTOCOL_HEADER_EXCEPT_FIRST_LEN
from client.events import EventManager, Event
from client.protobuf.dr2_login_pb2 import (
    pbreq_salt as PBReqSalt,  # type: ignore[attr-defined]
    pbrsp_salt as PBRspSalt,  # type: ignore[attr-defined]
    pbreq_echo as PBReqEcho,  # type: ignore[attr-defined]
    pbrsp_echo as PBRspEcho,  # type: ignore[attr-defined]
)


class IHNetClient:
    def __init__(self, host: str, port: int, timeout: float = 10.0):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.reader: asyncio.StreamReader | None = None
        self.writer: asyncio.StreamWriter | None = None

        _client_src_dir = os.path.dirname(os.path.abspath(__file__))
        self.event_manager = EventManager(os.path.join(_client_src_dir, "assets", "events.json"))
        self.sid = 0

    async def connect(self):
        self.reader, self.writer = await asyncio.wait_for(
            asyncio.open_connection(self.host, self.port), timeout=self.timeout
        )

    async def disconnect(self):
        if self.writer:
            self.writer.close()
            await self.writer.wait_closed()
            self.reader = None
            self.writer = None

    def _build_packet(self, group: int, cmd: int, sid: int, payload: bytes) -> bytes:
        after_len = CONFIG_PROTOCOL_HEADER_EXCEPT_FIRST_LEN + len(payload)
        return struct.pack(">HBBH", after_len, group & 0xFF, cmd & 0xFF, sid & 0xFFFF) + payload

    async def send(self, data: bytes):
        if not self.writer:
            raise ConnectionError("Not connected to server.")
        self.writer.write(data)
        await self.writer.drain()

    async def submit(self, event: Event, payload: bytes, buffer_size: int = -1) -> bytes:
        packet = self._build_packet(event.cmd_group, event.cmd_id, self.sid, payload)
        await self.send(packet)

        rcv_data = await self.receive(buffer_size)

        if len(rcv_data) == 0:
            raise ConnectionError("Connection unexpectedly closed by server.")

        return rcv_data

    async def receive(self, n: int = -1) -> bytes:
        if not self.reader:
            raise ConnectionError("Not connected to server.")
        return await asyncio.wait_for(self.reader.read(n), timeout=self.timeout)

