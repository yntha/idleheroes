import asyncio

from argparse import ArgumentParser

from client.ihnet import IHNetClient, IHNetError, NetClientStatus


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
            print(f"[App] Logged in as: {player.get_player().name} (UID: {client.local_player.get_uid()})")
            print(f"[App] Gold: {player_bag.get_gold()} | Gems: {player_bag.get_gems()} | XP: {player_bag.get_player_xp()}")

        await client.run_forever()
    except IHNetError as e:
        print(f"[App] Error: {e}")
    finally:
        print("[App] Disconnecting...")
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