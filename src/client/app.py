import asyncio

from client.ihnet import IHNetClient
from client.protobuf.dr2_login_pb_pb2 import pbrsp_echo


async def main():
    client = await IHNetClient.create_from_config()

    try:
        print("Sending 5 echo requests...")
        for i in range(5):
            echo = await client.echo()
            print(f"Echo response {i+1}: echo={echo.echo}")
    finally:
        await client.disconnect()

def cli_entry():
    asyncio.run(main())


if __name__ == '__main__':
    cli_entry()