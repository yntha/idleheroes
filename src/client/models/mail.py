from __future__ import annotations

from enum import Enum
from dataclasses import dataclass
from typing import TYPE_CHECKING

from google.protobuf.json_format import MessageToDict

from client.models.item_types import ItemTypeManager
from client.models.mail_types import MailTypeManagerInstance, Mail
from client.models.bag import IHBag

if TYPE_CHECKING:
    from client.protobuf.dr2_logic_pb_pb2 import pbrsp_sync
    from client.protobuf.dr2_comm_pb_pb2 import pb_mail


class MailOpType(Enum):
    DELETE = 1
    READ = 2
    CLAIM = 3
    BLOCK = 4

@dataclass
class IHMail:
    mail_id: int
    flag: int
    send_time: int
    mail_object: Mail
    affix: IHBag | None = None
    sender: str = ""

    @classmethod
    def from_sync(cls, sync: pbrsp_sync) -> list[IHMail]:
        mails = []
        mail_type_manager = MailTypeManagerInstance

        for mail in sync.mails:
            mail_object = mail_type_manager[mail.id]
            if mail_object is None:
                continue

            affix = None
            if mail.affix:
                affix = IHBag.from_pb(mail.affix)

            # protobuf excluded the 'from' field, so we must
            # do some extra work to recover the sender name
            mail_dict = MessageToDict(mail, preserving_proto_field_name=True)
            sender = mail_dict.get("from", "")

            mails.append(cls(
                mail_id=mail.mid,
                flag=mail.flag,
                send_time=mail.send_time,
                mail_object=mail_object,
                affix=affix,
                sender=sender
            ))
        return mails

    @classmethod
    def from_pb(cls, pb_mail: pb_mail) -> IHMail | None:
        mail_type_manager = MailTypeManagerInstance
        mail_object = mail_type_manager[pb_mail.id]
        if mail_object is None:
            return None

        affix = None
        if pb_mail.affix:
            affix = IHBag.from_pb(pb_mail.affix)

        # protobuf excluded the 'from' field, so we must
        # do some extra work to recover the sender name
        mail_dict = MessageToDict(pb_mail, preserving_proto_field_name=True)
        sender = mail_dict.get("from", "")

        return cls(
            mail_id=pb_mail.mid,
            flag=pb_mail.flag,
            send_time=pb_mail.send_time,
            mail_object=mail_object,
            affix=affix,
            sender=sender
        )

    def __repr__(self) -> str:
        affix_str = ""
        from_str = self.sender if self.sender else self.mail_object.sender

        if self.affix:
            affix_items = []
            for item in self.affix.items:
                item_type = ItemTypeManager()[item.item_id]
                if item_type:
                    affix_items.append(f"{item_type.name} x{item.count}")
                else:
                    affix_items.append(f"Unknown Item (ID: {item.item_id}) x{item.count}")
            affix_str = f", Affix: [{', '.join(affix_items)}]"
        claimed = " (Claimed)" if self.flag != 0 else ""
        return f"Mail(ID: {self.mail_id}, Name: {self.mail_object.name}, From: {from_str}{affix_str}{claimed})"