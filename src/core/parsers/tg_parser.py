import json

import pandas as pd

from src.models.mes_parser import MessagesParser
from src.models.exceptions import NoChatLoaded


class TelegramParser(MessagesParser):

    def __init__(self, file_path: str):

        self.file_path = file_path
        self.messages_df: pd.DataFrame | None = None

    def load_messages(self):

        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            records = []

        for message in data["messages"]:

            date = message["date"][:10]
            time = message["date"][12:]

            records.append([date, time, message["from"]])

        self.messages_df = pd.DataFrame(records, columns=["Date", "Time", "Sender"])

    def total_messages(self) -> int:
        if self.messages_df is None:
            raise NoChatLoaded

        messages: int = len(self.messages_df)

        return messages

    def participants(self) -> list[str]:
        if self.messages_df is None:
            raise NoChatLoaded

        participants: list[str] = sorted(list(set(self.messages_df["Sender"])))

        return participants

    def messages_per_participant(
        self, date=None, participant=None
    ) -> dict[str, int] | int:
        if self.messages_df is None:
            raise NoChatLoaded

        if participant is None and date is None:
            return self.messages_df["Sender"].value_counts().to_dict()

        if date is None:
            return self.messages_df["Sender"].value_counts()[participant]

        participants = self.participants()

        messages = self.messages_df.to_numpy()

        result = dict((p, 0) for p in participants)

        for message in messages:
            if message[0] == date:
                result[message[2]] += 1

        if participant is not None:
            return result[participant]

        return result
