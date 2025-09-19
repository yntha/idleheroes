import json

from dataclasses import dataclass

from client.constants import ROOT_DIR


@dataclass
class Item:
    id: int
    name: str
    brief: str
    explain: str


class ItemTypeManager:
    _JSON_FILE = "item_types.json"

    def __init__(self):
        self._item_type_map: dict[str, Item] = self._load_item_types()

    def _load_item_types(self):
        with open(ROOT_DIR / "client" / "assets" / self._JSON_FILE) as f:
            return {
                item["id"]: Item(
                    id=item["id"],
                    name=item["name"],
                    brief=item["brief"],
                    explain=item["explain"]
                ) for item in json.load(f)
            }

    def __getitem__(self, item_id: int) -> Item | None:
        return self._item_type_map.get(str(item_id), None)

    def get_item_name(self, item_id: int) -> str:
        item = self[item_id]
        return item.name if item else "Unknown Item"

    def get_item_description(self, item_id: int) -> str:
        item = self[item_id]
        return item.explain if item else "No description available."

    def get_item_short_desc(self, item_id: int) -> str:
        item = self[item_id]
        return item.brief if item else "No short description available."
