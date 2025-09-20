import json

from dataclasses import dataclass

from client.constants import ROOT_DIR


@dataclass
class Mail:
    id: int
    name: str
    content: str
    sender: str


class MailTypeManager:
    _JSON_FILE = "mail_types.json"

    def __init__(self):
        self._mail_type_map: dict[str, Mail] = self._load_mail_types()

    def _load_mail_types(self):
        with open(ROOT_DIR / "src" / "client" / "assets" / self._JSON_FILE, encoding="utf-8") as f:
            mail_data = json.load(f)

            return {
                mail_entry: Mail(
                    id=int(mail_entry),
                    name=mail_data[mail_entry]["name"],
                    content=mail_data[mail_entry]["content"],
                    sender=mail_data[mail_entry]["from"]
                ) for mail_entry in mail_data
            }

    def __getitem__(self, mail_id: int) -> Mail | None:
        return self._mail_type_map.get(str(mail_id), None)

    def get_mail_name(self, mail_id: int) -> str:
        mail = self[mail_id]
        return mail.name if mail else "Unknown Mail"

    def get_mail_content(self, mail_id: int) -> str:
        mail = self[mail_id]
        return mail.content if mail else "No content available."

    def get_mail_sender(self, mail_id: int) -> str:
        mail = self[mail_id]
        return mail.sender if mail else "Unknown Sender"
