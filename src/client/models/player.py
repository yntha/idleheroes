from dataclasses import dataclass


@dataclass
class PlayerAccount:
    account_email: str
    password: str
    uid: int = 0
