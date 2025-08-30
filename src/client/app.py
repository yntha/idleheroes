import asyncio

from client.ihnet import IHNetClient
from client.protobuf.dr2_login_pb_pb2 import pbrsp_echo


async def main():
    client = await IHNetClient.create_from_config()

    try:
        echo: pbrsp_echo = await client.echo()

        print(f"Echo response: {echo.echo}")
    finally:
        await client.disconnect()

def cli_entry():
    asyncio.run(main())


if __name__ == '__main__':
    cli_entry()