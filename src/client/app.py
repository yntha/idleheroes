import asyncio
import os.path
import sys

from typing import Any
from argparse import ArgumentParser
from http import HTTPStatus

import aiohttp

from google.protobuf.json_format import MessageToJson
from client.ihnet import IHNetClient
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
    dev_file = os.path.join(ROOT_DIR, ".dev")
    return os.path.exists(dev_file)


def _get_human_readable_size(size: int) -> str:
    if size == 0:
        return "0B"

    units = ["B", "KB", "MB", "GB"]
    unit_idx = 0
    size_f = float(size)

    while size_f >= 1024.0 and unit_idx < len(units) - 1:
        size_f /= 1024.0
        unit_idx += 1

    return f"{size_f:.2f}{units[unit_idx]}"


# fetch update file from GitHub releases
async def download_update(url: str) -> int:
    timeout_cfg = aiohttp.ClientTimeout(sock_connect=10.0, sock_read=10.0)

    async with aiohttp.ClientSession(timeout=timeout_cfg) as session:
        async with session.get(url, allow_redirects=True) as resp:
            if resp.status != HTTPStatus.OK:
                return resp.status

            total_size = int(resp.headers.get("Content-Length", "0"))
            dest_path = os.path.join(ROOT_DIR, "updates", f"ihres_{os.path.basename(url)}")

            # download to root/updates/ihres_<version>.zip
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            print(f"Downloading {url} ({_get_human_readable_size(total_size)})", end="")

            downloaded = 0
            dots = 0
            with open(dest_path, "wb") as f:
                async for chunk in resp.content.iter_chunked(1024 * 32):  # 32KB
                    f.write(chunk)
                    downloaded += len(chunk)

                    dots = (dots + 1) % 3
                    sys.stdout.write("\r" + "." * (dots + 1) + "   ")
                    sys.stdout.flush()

    print(f"\nDownload complete: {dest_path}")
    return HTTPStatus.OK


async def main():
    is_developer = _check_dev_file()
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
            raise ClientAppError("Salt request failed.")

        print("Logging in...", end="")
        login = await client.login(salt.salt)

        if config.debug:
            print(f"\nLogin response: {MessageToJson(login)}")
        else:
            print_result(login)

        if login.status != 0:
            raise ClientAppError("Login failed.")

        print("Authenticating...", end="")
        auth = await client.auth(login.uid, login.session)

        if config.debug:
            print(f"\nAuth response: {MessageToJson(auth)}")
        else:
            print_result(auth)

        if auth.status != 0:
            raise ClientAppError("Authentication failed.")

        print("Checking for updates...", end="")
        up = await client.up()

        if config.debug:
            print(f"\nUpdate response: {MessageToJson(up)}")
        else:
            print_result(up)

        if up.status != 0:
            raise ClientAppError("Update check failed.")

        if config.version != up.vsn:
            print(f"New version available: {config.version} -> {up.vsn}")

            if not is_developer:
                status = await download_update(f"https://github.com/yntha/idleheroes/releases/download/{up.vsn}/ihres_{up.vsn}.zip")

                if status == HTTPStatus.NOT_FOUND:
                    print("Resource update not released yet. Please try again later.")
            else:
                update_file = os.path.join(ROOT_DIR, ".update")

                with open(update_file, "w", encoding="utf-8") as f:
                    f.write(MessageToJson(up))

                print(f"Wrote update info to {update_file}")

        print("Synchronizing game state...", end="")
        sync = await client.sync()

        if config.debug:
            print(f"\nSync response: {MessageToJson(sync)}")
        else:
            print_result(sync)

        if sync.status != 0:
            raise ClientAppError("Sync failed.")
    except ClientAppError as e:
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