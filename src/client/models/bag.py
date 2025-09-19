from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from client.protobuf.dr2_logic_pb_pb2 import pbrsp_sync


GOLD_ITEM_ID = 1
GEM_ITEM_ID = 2
EXP_ITEM_ID = 3


@dataclass
class IHBagItem:
    item_id: int
    count: int


@dataclass
class IHBagEquipment:
    item_id: int
    num: int


@dataclass
class IHPlayerBag:
    items: list[IHBagItem]
    equipment: list[IHBagEquipment]

    @classmethod
    def from_sync(cls, sync: pbrsp_sync) -> IHPlayerBag:
        items = [IHBagItem(item_id=it.id, count=it.num) for it in sync.bag.items]
        equipment = [IHBagEquipment(item_id=eq.id, num=eq.num) for eq in sync.bag.equips]
        return cls(items=items, equipment=equipment)

    def get_item_by_type(self, item_type: int) -> IHBagItem | None:
        for item in self.items:
            if item.item_id == item_type:
                return item
        return None

    def get_gold(self) -> int:
        gold_item = self.get_item_by_type(GOLD_ITEM_ID)
        return gold_item.count if gold_item else 0

    def get_gems(self) -> int:
        gem_item = self.get_item_by_type(GEM_ITEM_ID)
        return gem_item.count if gem_item else 0

    def get_player_xp(self) -> int:
        xp_item = self.get_item_by_type(EXP_ITEM_ID)
        return xp_item.count if xp_item else 0
