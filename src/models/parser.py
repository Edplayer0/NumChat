from abc import ABC, abstractmethod


class MessagesParser(ABC):

    @abstractmethod
    def load_messages(self, file_path: str):
        """Load the messages from an exported file to a DataFrame.

        Args:
            file_path (str): the path to the selected chat.
        Returns:
            messages_df (DataFrame): the messages dataframe.
        """
