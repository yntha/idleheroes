import asyncio
import struct
import contextlib

from dataclasses import dataclass

from client.constants import (
    CONFIG_PROTOCOL_HEADER_LEN_RECV,
    CONFIG_PROTOCOL_HEADER_FIRST_FIELD_LEN
)
from client.utils import Utils
from client.config import ClientConfig


# constants
TYPE_EXT_OFFSET = 63  # command type offset for extended types (type > 63)
MIN_TYPE_NUM = 0
MAX_TYPE_NUM = 100
MIN_CMD_NUM = 0
MAX_CMD_NUM = 1000  # ??? should be 255, but the developers of idle heroes are monkeys apparently


@dataclass
class Frame:
    cmd_type: int
    cmd_id: int
    payload: bytes
    raw: bytes  # full raw frame including header


class TCPClient:
    def __init__(self, config: ClientConfig):
        self.config = config

        self.host: str | None = None
        self.port: int | None = None
        self.reader: asyncio.StreamReader | None = None
        self.writer: asyncio.StreamWriter | None = None
        self.read_task: asyncio.Task | None = None

        self._is_connected: asyncio.Event = asyncio.Event()

        # receive buffer for incomplete frames
        self._rx = bytearray()
        self.message_queue: asyncio.Queue[Frame] = asyncio.Queue()

    async def connect(self, host: str, port: int, timeout: float = 10.0):
        self.host = host
        self.port = port
        self.reader, self.writer = await asyncio.wait_for(
            asyncio.open_connection(host, port), timeout=timeout
        )

        self._is_connected.set()
        self.read_task = asyncio.create_task(self._read_loop())

    async def disconnect(self):
        if self.read_task is not None:
            self.read_task.cancel()

            with contextlib.suppress(asyncio.CancelledError):
                await self.read_task

            self.read_task = None

        if self.writer is not None:
            self.writer.close()
            await self.writer.wait_closed()
            self.writer = None
            self.reader = None

        self._is_connected.clear()

    async def send(self, data: bytes):
        if not self._is_connected.is_set() or self.writer is None:
            raise ConnectionError("Not connected to server.")

        if self.config.debug:
            print(f"Sending {len(data)} bytes:\n{Utils.hexdump(data)}\n")

        self.writer.write(data)
        await self.writer.drain()

    async def _read_loop(self):
        while True:
            try:
                if not self._is_connected.is_set() or self.reader is None:
                    raise ConnectionError("Not connected to server.")

                chunk = await self.reader.read(4096)

                if self.config.debug:
                    print(f"Received {len(chunk)} bytes:\n{Utils.hexdump(chunk)}\n")

                if len(chunk) == 0:
                    raise ConnectionError("Connection unexpectedly closed by server.")

                self._rx.extend(chunk)

                for frame in self._process_rx():
                    await self.message_queue.put(frame)
            except Exception as e:
                break

        if self._is_connected.is_set():
            await self.disconnect()

    def _decode_type(self, raw_type: int) -> int:
        return raw_type - TYPE_EXT_OFFSET if raw_type > TYPE_EXT_OFFSET else raw_type

    def _process_rx(self):
        out = []
        buf = self._rx
        offset = 0

        while len(buf) - offset >= CONFIG_PROTOCOL_HEADER_LEN_RECV:
            rcv_len = struct.unpack_from(">H", buf, offset)[0]
            total_len = rcv_len + CONFIG_PROTOCOL_HEADER_FIRST_FIELD_LEN

            if len(buf) - offset < total_len:
                break  # wait for more data; incomplete frame

            frame = bytes(buf[offset:offset + total_len])
            offset += total_len

            rcv_type = self._decode_type(frame[2])
            rcv_id = frame[3]

            if rcv_type > 63:
                rcv_type -= 63

            # header validation
            if not (MIN_TYPE_NUM <= rcv_type <= MAX_TYPE_NUM) or not (MIN_CMD_NUM <= rcv_id <= MAX_CMD_NUM):
                self._rx.clear()  # protocol error, discard all data
                return out

            payload = frame[CONFIG_PROTOCOL_HEADER_LEN_RECV:]
            out.append(Frame(cmd_type=rcv_type, cmd_id=rcv_id, payload=payload, raw=frame))

        # remove processed data from buffer
        if offset > 0:
            del self._rx[:offset]

        return out
