from __future__ import annotations

class Utils:
    @staticmethod
    def get_cmd_name(cmd_group: int, cmd_type: int) -> str:
        return f"EVENT_CMD_{cmd_group}_{cmd_type}"

    @staticmethod
    def hexdump(data: bytes,
                formatted: bool = True,
                col_len: int = 1,
                row_len: int = 16,
                sep: str = ' ',
                show_offset: bool = True,
                show_header: bool = True
                ) -> str:
        """Returns a hexdump of the underlying buffer, optionally including offsets and a lateral header."""

        # If no formatting is required, just return the plain hex string.
        if not formatted:
            return data.hex()

        # row_len should be divisible by col_len
        if row_len % col_len:
            raise ValueError("hexdump: col_len must be a multiple of row_len.")

        stream_data = data
        dump = ''
        last_line_len = 0

        # Determine the width of the offset field based on the data size, ensuring it's even
        offset_field_width = len(f"{len(stream_data):x}") + 1
        if offset_field_width % 2 != 0:
            offset_field_width += 1

        # Add lateral header row if enabled
        if show_header:
            header = ("=" * offset_field_width if show_offset else "") + "  "  # Use '=' to occupy leading space
            for i in range(row_len):
                if i % col_len == 0 and i != 0:
                    header += sep
                header += f" {i % 16:X}"  # Replace leading 0 with a space
            dump += header + '\n'

        # Split the data into chunks of row_len
        d, m = divmod(len(stream_data), row_len)
        chunks = []
        for i in range(d):
            chunks.append(stream_data[i * row_len : (i + 1) * row_len])
        if m:
            chunks.append(stream_data[d * row_len :])

        # Process each chunk
        for i, chunk in enumerate(chunks):
            # Build the offset string if enabled
            offset_str = f"{i * row_len:0{offset_field_width}x}" if show_offset else ""

            # Build the hex part of this line
            row = ''
            for j, b in enumerate(chunk):
                # Add a separator after each col_len bytes
                if j != 0 and (j % col_len) == 0:
                    row += sep
                row += f"{b:02x}"

            # If current line is shorter than the previous line, pad it
            if len(row) < last_line_len:
                row += ' ' * (last_line_len - len(row))

            # Add offset and hex data to the dump
            dump += f"{offset_str}  {row}    " if show_offset else f"{row}    "
            last_line_len = len(row)

            # Append ASCII representation (printable chars or '.')
            for b in chunk:
                # 0x20 (space) through 0x7E (~) are generally considered "printable"
                if 0x20 <= b < 0x7f:
                    dump += chr(b)
                else:
                    dump += '.'

            dump += '\n'

        return dump.strip()

    @classmethod
    def _read_varint(cls, b: bytes, i: int) -> tuple[int, int]:
        shift = 0
        val = 0

        while True:
            if i >= len(b):
                raise EOFError(f"Truncated varint at {i}")

            byte = b[i]
            i += 1
            val |= (byte & 0x7F) << shift

            if (byte & 0x80) == 0:
                return val, i

            shift += 7

            if shift > 70:
                raise ValueError(f"Malformed varint at {i}")

    @classmethod
    def scan_wire(cls, b: bytes) -> str:
        out = [f"bytes={len(b)}"]
        i = 0

        while i < len(b):
            try:
                key, i2 = cls._read_varint(b, i)
            except Exception as e:
                out.append(f"ERR key at {i}: {e}")
                break

            field = key >> 3
            wtype = key & 7
            i = i2

            try:
                if wtype == 0:
                    val, i = cls._read_varint(b, i)
                    out.append(f"@{i2:04d} f={field} wt=VARINT v={val}")
                elif wtype == 1:
                    if i + 8 > len(b):
                        raise EOFError(f"Need 8 bytes, have {len(b) - i}")

                    out.append(f"@{i2:04d} f={field} wt=FIXED64 {b[i : i + 8].hex()}")
                    i += 8
                elif wtype == 2:
                    l, i = cls._read_varint(b, i)  # noqa: E741
                    if i + l > len(b):
                        raise EOFError(f"len={l}, have {len(b) - i}")

                    seg = b[i : i + l]
                    out.append(f"@{i2:04d} f={field} wt=LEN len={l} head={seg[:16].hex()}")
                    i += l
                elif wtype == 5:
                    if i + 4 > len(b):
                        raise EOFError(f"need 4 bytes, have {len(b) - i}")

                    out.append(f"@{i2:04d} f={field} wt=FIXED32 {b[i : i + 4].hex()}")
                    i += 4
                else:
                    out.append(f"@{i2:04d} f={field} wt={wtype} (unsupported)")
                    break
            except Exception as e:
                out.append(f"ERR value at {i}: {e}")
                break

        return "\n".join(out)