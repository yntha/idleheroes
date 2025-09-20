from __future__ import annotations

import json

from dataclasses import dataclass

from client.constants import ROOT_DIR


@dataclass
class Item:
    id: int
    name: str
    brief: str
    explain: str | None = None


class ItemTypeManager:
    _JSON_FILE = "item_types.json"

    def __init__(self):
        self._item_type_map: dict[str, Item] = self._load_item_types()

    def _load_item_types(self):
        with open(ROOT_DIR / "src" / "client" / "assets" / self._JSON_FILE) as f:
            item_data = json.load(f)
            item_type_map = {}

            for item_entry in item_data:
                item_type_map[item_entry] = Item(
                    id=int(item_entry),
                    name=item_data[item_entry]["name"],
                    brief=item_data[item_entry]["brief"],
                    explain=item_data[item_entry].get("explain")
                )

            return item_type_map

    def __getitem__(self, item_id: int) -> Item | None:
        return self._item_type_map.get(str(item_id), None)

    def get_item_name(self, item_id: int) -> str:
        item = self[item_id]
        return item.name if item else "Unknown Item"

    def get_item_description(self, item_id: int) -> str:
        item = self[item_id]

        if item is None:
            return "No description available."

        return item.explain if item.explain else "No description available."

    def get_item_short_desc(self, item_id: int) -> str:
        item = self[item_id]
        return item.brief if item else "No short description available."


ItemTypeManagerInstance = ItemTypeManager()
