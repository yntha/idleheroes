import asyncio

from typing import Any
from argparse import ArgumentParser

from google.protobuf.json_format import MessageToJson
from client.ihnet import IHNetClient


# enable debug output
DEBUG = False


def print_result(message: Any):
    if message.status == 0:
        print(" Success!")
    else:
        print(f" Failed! (status={message.status})")


async def main():
    client = await IHNetClient.create_from_config()
    account = client.get_account()
    config = client.client_config

    config.debug = DEBUG

    if not account.account or not account.password:
        print("Account details are incomplete or missing. Please set up your account:")

        account.account = input("Account: ").strip()
        account.password = input("Password: ").strip()

    try:
        # print("Sending 5 echo requests...")
        # for i in range(5):
        #     echo = await client.echo()
        #     print(f"Echo response {i+1}: {MessageToJson(echo)}")

        # might not be a good idea to spam registration requests
        # print("\nRegistering guest account...")
        # reg = await client.reg()
        # print(f"Registration response: {MessageToJson(reg)}")

        print("Requesting salt...", end="")
        salt = await client.salt()

        if config.debug:
            print(f"\nSalt response: {MessageToJson(salt)}")
        else:
            print_result(salt)

        if salt.status != 0:
            raise RuntimeError("Salt request failed.")

        print("Logging in...", end="")
        login = await client.login(salt.salt)

        if config.debug:
            print(f"\nLogin response: {MessageToJson(login)}")
        else:
            print_result(login)

        if login.status != 0:
            raise RuntimeError("Login failed.")

        print("Authenticating...", end="")
        auth = await client.auth(login.uid, login.session)

        if config.debug:
            print(f"\nAuth response: {MessageToJson(auth)}")
        else:
            print_result(auth)

        if auth.status != 0:
            raise RuntimeError("Authentication failed.")

        print("Checking for updates...", end="")
        up = await client.up()

        if config.debug:
            print(f"\nUpdate response: {MessageToJson(up)}")
        else:
            print_result(up)

        if up.status != 0:
            raise RuntimeError("Update check failed.")

        if config.version != up.vsn:
            print(f"Updating version {config.version} -> {up.vsn}")
            await client.update_version()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        await client.disconnect()


def cli_entry():
    parser = ArgumentParser(description="Idle Heroes Python Client")
    parser.add_argument(
        "-d", "--debug", action="store_true", help="Enable debug output"
    )

    args = parser.parse_args()
    global DEBUG
    DEBUG = args.debug

    asyncio.run(main())


if __name__ == '__main__':
    cli_entry()