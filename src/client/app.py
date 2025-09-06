import asyncio
from pathlib import Path
import json
import zipfile
import shutil

from typing import Any
from argparse import ArgumentParser
from http import HTTPStatus

import aiohttp
from urllib.parse import urlsplit

from google.protobuf.json_format import MessageToJson
from client.ihnet import IHNetClient
from client.constants import ROOT_DIR
from client.config import ClientConfig


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
async def download_update_file(url: str) -> int:
    timeout_cfg = aiohttp.ClientTimeout(sock_connect=10.0, sock_read=10.0)

    async with aiohttp.ClientSession(timeout=timeout_cfg) as session:
        async with session.get(url, allow_redirects=True) as resp:
            if resp.status != HTTPStatus.OK:
                return resp.status

            total_size = int(resp.headers.get("Content-Length", "0"))
            filename = Path(urlsplit(url).path).name
            dest_path = Path(ROOT_DIR) / "update" / filename

            # download to root/update/ihres_<version>.zip
            dest_path.parent.mkdir(parents=True, exist_ok=True)

            print(f"Downloading {url} ({_get_human_readable_size(total_size)})", end="")

            downloaded = 0
            progress_states = ["-", "\\", "|", "/"]
            terminal_width = shutil.get_terminal_size((80, 20)).columns
            with dest_path.open("wb") as f:
                async for chunk in resp.content.iter_chunked(1024 * 32):  # 32KB
                    f.write(chunk)
                    downloaded += len(chunk)

                    state = progress_states[(downloaded // (1024 * 32)) % len(progress_states)]
                    download_msg = (
                        f"\r[{state}] "
                        f"Downloading {url} ({_get_human_readable_size(total_size)})/{_get_human_readable_size(downloaded)}"
                    )
                    download_msg = download_msg.ljust(terminal_width - 1)
                    print(download_msg,end="", flush=True)

    return HTTPStatus.OK


async def download_update(config: ClientConfig, for_version: str) -> int:
    res_dir = Path(ROOT_DIR) / "res"
    status = await download_update_file(f"https://github.com/yntha/idleheroes/releases/download/{for_version}/ihres_{for_version}.zip")

    if status != HTTPStatus.OK:
        return status

    print("\nDownload complete. Extracting...")

    # extract to root
    zip_path = Path(ROOT_DIR) / "update" / f"ihres_{for_version}.zip"
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(ROOT_DIR)

    # get update info file
    update_info_path = res_dir / "ihres_update.json"
    if update_info_path.exists():
        with update_info_path.open("r", encoding="utf-8") as f:
            update_info = json.load(f)

            config.version = update_info["version"]
            config.save()

    # clean up
    try:
        zip_path.unlink()
    except FileNotFoundError:
        pass
    try:
        update_info_path.unlink()
    except FileNotFoundError:
        pass
    try:
        (Path(ROOT_DIR) / ".update").unlink()
    except FileNotFoundError:
        pass

    # delete the update folder
    try:
        (Path(ROOT_DIR) / "update").rmdir()
    except OSError:
        pass

    # delete the temp folder
    try:
        (Path(ROOT_DIR) / "temp").rmdir()
    except OSError:
        pass

    return status


async def check_resources(config: ClientConfig):
    res_dir = Path(ROOT_DIR) / "res"

    # if the res folder doesn't exist, that means the base resources are missing.
    # an update check comes after this, so resource download will be triggered twice
    # on first run.
    if not res_dir.exists():
        print("Missing resources. Downloading now...")
        status = await download_update(config, config.version)
        if status != HTTPStatus.OK:
            raise ClientAppError(f"Failed to download resources: HTTP {status}")

        print("Resources downloaded.")


async def main():
    is_developer = _check_dev_file()
    client = IHNetClient()
    account = client.get_account()
    config = client.client_config

    config.debug = DEBUG

    await check_resources(config)
    await client.init()

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
                status = await download_update(config, up.vsn)

                if status == HTTPStatus.NOT_FOUND:
                    print("Resource update not released yet. Please try again later.")
            else:
                update_file = Path(ROOT_DIR) / ".update"

                update_file.write_text(MessageToJson(up), encoding="utf-8")

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