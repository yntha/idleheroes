import asyncio

from client.ihnet import IHNetClient


async def main():
    client = await IHNetClient.create_from_config()

    try:
        print("Sending 5 echo requests...")
        for i in range(5):
            echo = await client.echo()
            print(f"Echo response {i+1}: echo={echo.echo}")

        print("\nRequesting salt...")
        salt = await client.salt()
        print(f"Salt response: status={salt.status} salt='{salt.salt}' uid={salt.uid} flag={salt.flag} cd={salt.cd}")
    finally:
        await client.disconnect()


def cli_entry():
    asyncio.run(main())


if __name__ == '__main__':
    cli_entry()