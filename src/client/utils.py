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