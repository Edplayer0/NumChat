import json

from src.models.mes_parser import MessagesParser
from src.models.exceptions import NoChatLoaded


class TelegramParser(MessagesParser):

    def __init__(self, file_path: str):

        self.file_path = file_path
        self.messages: dict[str, list] = {2025: [[20]]}

    def load_messages(self):

        with open(self.file_path, "r", encoding="utf-8") as file:
            messages = json.load(file)

        for message in messages:

            year = message["date"]
            month = message["month"]
            day = message["day"]

            self.messages[year][month - 1][day - 1] += 1

    def total_messages(self):
        if self.messages is None:
            raise NoChatLoaded

        return sum(self.messages)

    def participants(self):
        if self.messages is None:
            raise NoChatLoaded
