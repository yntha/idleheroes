import asyncio
from pathlib import Path

from typing import Any
from argparse import ArgumentParser

from client.ihnet import IHNetClient, IHNetError
from client.constants import ROOT_DIR


# enable debug output
DEBUG = False


class ClientAppError(Exception):
    pass


def print_result(message: Any):
    if message.status == 0:
        print(" Success!")
    else:
        print(f" Failed! (status={message.status})")


def _check_dev_file() -> bool:
    dev_file = Path(ROOT_DIR) / ".dev"
    return dev_file.exists()


async def main():
    client = IHNetClient()

    try:
        await client.init()
        player = client.local_player

        if player is not None:
            print(f"Logged in as: {player.get_player().name} (UID: {client.local_player.get_uid()})")

    except IHNetError as e:
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