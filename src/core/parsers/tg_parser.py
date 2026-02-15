import json

import pandas as pd

from src.models.parser import MessagesParser


class TelegramParser(MessagesParser):

    def load_messages(self, file_path: str) -> pd.DataFrame:

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        records = []

        for message in data["messages"]:

            if not message["type"] == "message":
                continue

            date = message["date"][:10]
            time = message["date"][11:]

            records.append([date, time, message["from"]])

        messages_df = self.to_dataframe(records)

        return messages_df
