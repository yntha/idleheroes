from __future__ import annotations

import zipfile
import shutil
import io

from enum import Enum
from http import HTTPStatus
from pathlib import Path
from typing import TYPE_CHECKING
from packaging import version

import aiohttp

from client.constants import ROOT_DIR

if TYPE_CHECKING:
    from client.config import ClientConfig


class UpdateType(Enum):
    NONE = 0
    PATCH = 1
    MINOR = 2
    MAJOR = 3


class Updater:
    """Handles discovery, download, and installation of resource update packages.

    Naming conventions for resource archives:
      Major base: ihres_<major>.x.x_base.zip
      Minor base: ihres_x.<minor>.x_base.zip
      Patch: ihres_<major>.<minor>.<patch>.zip
    Example: ihres_1.34.0.zip, ihres_1.34.x_base.zip, ihres_1.x.x_base.zip
    The extracted contents are merged into ROOT_DIR/<resources_dir> as specified in ClientConfig.
    """
    def __init__(self, config: ClientConfig):
        """Initialize with a ClientConfig and ensure resources directory exists.

        Args:
            config: Active client configuration object.
        """
        self.config = config

    async def ensure_resources_dir(self):
        """Ensure the base resources directory exists. If missing, download the latest minor base resources."""
        resources_dir = Path(ROOT_DIR) / self.config.resources_dir

        if not resources_dir.exists():
            version_parsed = version.parse(self.config.version)
            major_version = version_parsed.major
            minor_version = version_parsed.minor

            print(f"[Updater] Base resources directory does not exist! Downloading base resources ({major_version}.{minor_version})...")

            result = await self.check_for_update(version_parsed, UpdateType.MINOR)

            if result == UpdateType.NONE:
                raise RuntimeError("Failed to find base resources.")

            await self.install_minor_update(version_parsed)

    async def _head_ok(self, session: aiohttp.ClientSession, url: str) -> bool:
        """Perform a HEAD request and return True if the URL responds 200 OK.

        Args:
            session: Reusable aiohttp session.
            url: Candidate URL to probe.
        """
        try:
            async with session.head(url, allow_redirects=True) as resp:
                return resp.status == HTTPStatus.OK
        except Exception:
            return False

    def _get_human_readable_size(self, size: int) -> str:
        if size == 0:
            return "0B"

        units = ["B", "KB", "MB", "GB"]
        unit_idx = 0
        size_f = float(size)

        while size_f >= 1024.0 and unit_idx < len(units) - 1:
            size_f /= 1024.0
            unit_idx += 1

        return f"{size_f:.2f}{units[unit_idx]}"

    async def _resolve_download_url(self, session: aiohttp.ClientSession, new_version: version.Version, filename: str) -> str | None:
        """Resolve a download URL.

        Args:
            session: Active aiohttp session.
            new_version: The new version to download.
            filename: Archive filename to search.
        Returns:
            Resolved URL string or None if not reachable.
        """
        base = str(self.config.update_url).rstrip("/")
        url = f"{base}/{new_version}/{filename}"

        if await self._head_ok(session, url):
            return url

        return None

    async def _download_zip_bytes(self, url: str) -> bytes:
        """Download the zip file and return its raw bytes."""
        print(f"[Updater] Downloading: {url}...")

        async with aiohttp.ClientSession() as session:
            async with session.get(url, allow_redirects=True) as resp:
                if resp.status != HTTPStatus.OK:
                    raise RuntimeError(f"Download failed (HTTP {resp.status}) for {url}")

                data = await resp.read()

        print(f"[Updater] Downloaded {self._get_human_readable_size(len(data))}.")
        return data

    def _extract_zip_bytes(self, data: bytes):
        """Extract zip bytes directly into the resources directory via a staging temp dir.

        Extraction strategy:
          1. Inflate into a temp directory under ROOT_DIR/.res_tmp
          2. Merge into final resources directory
          3. Remove staging directory
        """
        print("[Updater] Extracting resources...")

        resources_dir = Path(ROOT_DIR) / self.config.resources_dir
        staging = Path(ROOT_DIR) / ".res_tmp"

        if staging.exists():
            shutil.rmtree(staging, ignore_errors=True)

        staging.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(io.BytesIO(data)) as zf:
            zf.extractall(staging)

        resources_dir.mkdir(parents=True, exist_ok=True)

        for item in staging.iterdir():
            dest = resources_dir / item.name

            if dest.exists():
                if dest.is_dir():
                    shutil.rmtree(dest, ignore_errors=True)
                else:
                    dest.unlink(missing_ok=True)

            if item.is_dir():
                shutil.copytree(item, dest)
            else:
                shutil.copy2(item, dest)

        shutil.rmtree(staging, ignore_errors=True)
        print(f"[Updater] Resources updated in {resources_dir}")

    async def check_for_update(self, new_version: version.Version, force_update: UpdateType = UpdateType.NONE) -> UpdateType:
        """Check availability of an update archive for the given target version.

        Chooses update type (MAJOR/MINOR/PATCH) based on semantic version difference
        from the currently installed version unless force_update overrides it. Builds
        the appropriate archive filename pattern, resolves its download URL, and
        returns the determined update type if the file exists, otherwise NONE.

        Args:
            new_version (version.Version): Target version to update to.
            force_update (UpdateType): Optional override for desired update type
                (MAJOR, MINOR, PATCH); defaults to NONE (auto-detect).
            UpdateType: MAJOR, MINOR, PATCH if a corresponding archive is found;
                otherwise NONE.
        Returns:
            Available update type (MAJOR/MINOR/PATCH) or NONE if not found.
        """
        current_version = version.parse(self.config.version)

        if new_version.major != current_version.major or force_update == UpdateType.MAJOR:
            filename = f"ihres_{new_version.major}.x.x_base.zip"
            update_type = UpdateType.MAJOR
            new_version = version.Version(f"{new_version.major}.0.0")
        elif new_version.minor != current_version.minor or force_update == UpdateType.MINOR:
            filename = f"ihres_{new_version.major}.{new_version.minor}.x_base.zip"
            update_type = UpdateType.MINOR
            new_version = version.Version(f"{new_version.major}.{new_version.minor}.0")
        elif force_update == UpdateType.PATCH:  # redundant, i know
            filename = f"ihres_{new_version.major}.{new_version.minor}.{new_version.micro}.zip"
            update_type = UpdateType.PATCH
        else:
            filename = f"ihres_{new_version.major}.{new_version.minor}.{new_version.micro}.zip"
            update_type = UpdateType.PATCH

        async with aiohttp.ClientSession() as session:
            url = await self._resolve_download_url(session, new_version, filename)

            if not url:
                print(f"[Updater] Resource file '{filename}' not available yet.")
                return UpdateType.NONE

            print(f"[Updater] Found {new_version} update package.")
            return force_update if force_update != UpdateType.NONE else update_type

    async def install_major_update(self, new_version: version.Version, filename: str | None = None):
        """Download and install the latest major base resource archive for new_version."""
        if filename is None:
            filename = f"ihres_{new_version.major}.x.x_base.zip"

        async with aiohttp.ClientSession() as session:
            url = await self._resolve_download_url(session, new_version, filename)

            if not url:
                raise RuntimeError(f"[Updater] Major base resource '{filename}' not found.")

        data = await self._download_zip_bytes(url)
        self._extract_zip_bytes(data)

    async def install_minor_update(self, new_version: version.Version, filename: str | None = None):
        """Download and install the latest minor base resource archive for new_version."""
        if filename is None:
            filename = f"ihres_{new_version.major}.{new_version.minor}.x_base.zip"

        async with aiohttp.ClientSession() as session:
            url = await self._resolve_download_url(session, new_version, filename)

            if not url:
                raise RuntimeError(f"[Updater] Minor base resource '{filename}' not found.")

        data = await self._download_zip_bytes(url)
        self._extract_zip_bytes(data)

    async def install_patch_update(self, new_version: version.Version, filename: str | None = None):
        """Download and install a patch resource archive for the exact new_version."""
        if filename is None:
            filename = f"ihres_{new_version.major}.{new_version.minor}.{new_version.micro}.zip"

        async with aiohttp.ClientSession() as session:
            url = await self._resolve_download_url(session, new_version, filename)

            if not url:
                raise RuntimeError(f"[Updater] Patch resource '{filename}' not found.")

        data = await self._download_zip_bytes(url)
        self._extract_zip_bytes(data)

