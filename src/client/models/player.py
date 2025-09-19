from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from client.models.bag import IHPlayerBag

if TYPE_CHECKING:
    from client.protobuf.dr2_logic_pb_pb2 import pbrsp_sync


@dataclass
class IHPlayer:
    name: str
    logo: int
    guild_id: int = 0
    guild_name: str = ""
    border: int = 0
    guild_level: int = 0
    country: str = ""
    sds: str = ""  # social data string?
    city: str = ""

    @classmethod
    def from_sync(cls, sync: pbrsp_sync) -> IHPlayer:
        return cls(
            name=sync.player.name,
            logo=sync.player.logo,
            guild_id=sync.player.gid,
            guild_name=sync.player.gname,
            border=sync.player.border,
            guild_level=sync.player.glv,
            country=sync.player.country,
            sds=sync.player.sds,
            city=sync.player.city,
        )


class LocalPlayer:
    def __init__(self):
        self._uid: int = 0
        self._session: str = ""
        self._sid: int = 0
        self.player: IHPlayer | None = None
        self.bag: IHPlayerBag | None = None

    def get_uid(self) -> int:
        return self._uid

    def get_session(self) -> str:
        return self._session

    def get_sid(self) -> int:
        return self._sid

    def get_player(self) -> IHPlayer:
        if self.player is None:
            raise ValueError("Player is not set")

        return self.player

    def get_bag(self) -> IHPlayerBag:
        if self.bag is None:
            raise ValueError("Bag is not set")
        return self.bag

    def set_uid(self, uid: int):
        self._uid = uid

    def set_session(self, session: str):
        self._session = session

    def set_sid(self, sid: int):
        self._sid = sid

    def set_player_from_sync(self, sync_rsp: pbrsp_sync):
        self.player = IHPlayer.from_sync(sync_rsp)

    def set_bag_from_sync(self, sync_rsp: pbrsp_sync):
        self.bag = IHPlayerBag.from_sync(sync_rsp)
