import json

from dataclasses import dataclass


@dataclass
class Event:
    cmd: str
    cmd_group: int
    cmd_type: int
    cmd_name: str


class EventManager:
    def __init__(self, event_file: str):
        self.events: dict[str, Event] = {}
        self.load_events(event_file)
        self.push_events = [
            self.get_event("EVENT_CMD_5_0"),  # push_mail
        ]

    def load_events(self, event_file: str):
        with open(event_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            for event_data in data:
                event = Event(**event_data)
                self.events[event.cmd_name] = event

    def get_event(self, cmd_name: str) -> Event:
        return self.events[cmd_name]
