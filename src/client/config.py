from __future__ import annotations

import json
import os

from enum import StrEnum
from dataclasses import dataclass, asdict
from client.constants import ROOT_DIR


# ../../config
CONFIG_DIR = os.path.join(ROOT_DIR, "config")


class TimeUnit(StrEnum):
    SECONDS = "seconds"
    MINUTES = "minutes"
    HOURS = "hours"


@dataclass
class ClientConfig:
    gateway_host: str
    gateway_port: int
    conn_timeout: float
    debug: bool
    version: str
    update_url: str
    resources_dir: str

    @classmethod
    def get(cls) -> ClientConfig:
        config_path = os.path.join(CONFIG_DIR, "config.json")

        if not os.path.exists(config_path):
            config = cls.get_default()
            config.save()

            return config

        with open(config_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls(**data)

    @classmethod
    def get_default(cls) -> ClientConfig:
        return cls(
            gateway_host="adgp.gate-dhgames.com",
            gateway_port=5000,
            conn_timeout=10.0,
            debug=False,
            version="1.34.0",
            update_url="https://github.com/yntha/idleheroes/releases/download",
            resources_dir="res/"
        )

    def save(self):
        config_path = os.path.join(CONFIG_DIR, "config.json")

        os.makedirs(CONFIG_DIR, exist_ok=True)

        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(asdict(self), f, indent=4)


@dataclass
class AccountConfig:
    account: str
    password: str

    @classmethod
    def get(cls) -> AccountConfig:
        config_path = os.path.join(CONFIG_DIR, "account.json")

        if not os.path.exists(config_path):
            config = cls.get_default()
            config.save()

            return config

        with open(config_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls(**data)

    @classmethod
    def get_default(cls) -> AccountConfig:
        return cls(
            account="",
            password="",
        )

    def save(self):
        config_path = os.path.join(CONFIG_DIR, "account.json")

        os.makedirs(CONFIG_DIR, exist_ok=True)

        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(asdict(self), f, indent=4)


@dataclass
class FarmConfig:
    autobattle_interval: float
    autobattle_interval_timeunit: TimeUnit

    @classmethod
    def _get_seconds_multiplier(cls, timeunit: TimeUnit) -> float:
        if timeunit == TimeUnit.SECONDS:
            return 1.0
        elif timeunit == TimeUnit.MINUTES:
            return 60.0
        elif timeunit == TimeUnit.HOURS:
            return 3600.0
        else:
            raise ValueError(f"Invalid TimeUnit: {timeunit}")

    @classmethod
    def get(cls) -> FarmConfig:
        config_path = os.path.join(CONFIG_DIR, "farm.json")

        if not os.path.exists(config_path):
            config = cls.get_default()
            config.save()

            return config

        with open(config_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            data["autobattle_interval_timeunit"] = TimeUnit(data["autobattle_interval_timeunit"])
            data["autobattle_interval"] = float(data["autobattle_interval"]) * cls._get_seconds_multiplier(data["autobattle_interval_timeunit"])
        return cls(**data)

    @classmethod
    def get_default(cls) -> FarmConfig:
        return cls(
            autobattle_interval=5.0,
            autobattle_interval_timeunit=TimeUnit.MINUTES,
        )

    def save(self):
        config_path = os.path.join(CONFIG_DIR, "farm.json")

        os.makedirs(CONFIG_DIR, exist_ok=True)

        with open(config_path, "w", encoding="utf-8") as f:
            data = asdict(self)
            data["autobattle_interval_timeunit"] = self.autobattle_interval_timeunit.value
            data["autobattle_interval"] = self.autobattle_interval / self._get_seconds_multiplier(self.autobattle_interval_timeunit)
            json.dump(data, f, indent=4)

    def get_autobattle_interval_str(self) -> str:
        return f"{self.autobattle_interval / self._get_seconds_multiplier(self.autobattle_interval_timeunit):.2f} {self.autobattle_interval_timeunit.value.lower()}"
