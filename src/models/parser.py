from abc import ABC, abstractmethod
import pandas as pd


class MessagesParser(ABC):

    @abstractmethod
    def load_messages(self, file_path: str):
        """Load the messages from an exported file to a DataFrame.

        Args:
            file_path (str): the path to the selected chat.
        Returns:
            messages_df (DataFrame): the messages dataframe.
        """

    def to_dataframe(self, values: list):
        messages_df = pd.DataFrame(values, columns=["Date", "Time", "Sender"])
        messages_df["Sender"] = messages_df["Sender"].astype("category")

        return messages_df
