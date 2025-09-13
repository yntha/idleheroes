from dataclasses import dataclass


@dataclass
class LocalPlayer:
    uid: int = 0
    session: str = ""
    sid: int = 0
