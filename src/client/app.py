import asyncio

from argparse import ArgumentParser

from google.protobuf.json_format import MessageToDict

from client.ihnet import IHNetClient, IHNetError, NetClientStatus
from client.models.mail import MailOpType
from client.protobuf.dr2_logic_pb_pb2 import pbrsp_op_mail


# enable debug output
DEBUG = False


class ClientAppError(Exception):
    pass


async def main():
    client = IHNetClient()
    client.client_config.debug = DEBUG

    try:
        result = await client.init()

        if result == NetClientStatus.UPDATE_NOT_READY:
            await client.disconnect()
            return

        player = client.local_player
        player_bag = player.get_bag()

        if player is not None:
            print(f"Logged in as: {player.get_player().name} (UID: {client.local_player.get_uid()})")
            print(f"Gold: {player_bag.get_gold()} | Gems: {player_bag.get_gems()} | XP: {player_bag.get_player_xp()}")

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