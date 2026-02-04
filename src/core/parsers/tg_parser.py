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

        participants: list[str] = sorted(self.messages_df["Sender"].unique())

        return participants

    def messages_per_participant(
        self, date=None, participant=None
    ) -> dict[str, int] | int:

        if self.messages_df is None:
            raise NoChatLoaded

        # No data specified
        if participant is None and date is None:
            return self.messages_df["Sender"].value_counts().to_dict()

        # Participant specified
        if date is None:
            mask = self.messages_df["Sender"].values == participant
            return mask.sum()

        # Date specified
        if participant is None:
            mask = self.messages_df["Date"].str.startswith(date)
            return mask.sum()

        # Both specified
        mask = (self.messages_df["Sender"].values == participant) & (
            self.messages_df["Date"].str.startswith(date)
        )

        return mask.sum()
