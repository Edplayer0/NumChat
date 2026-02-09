from typing import Optional

import pandas as pd

from src.models.exceptions import NoChatLoaded


class Analizer:

    def __new__(cls) -> "Analizer":
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._current_participant: Optional[str] = None

    @property
    def messages_df(self):
        """Returns the messages dataframe if its loaded,
        otherwise raise NoChatLoaded exception"""

        if not hasattr(self, "_messages_df"):
            raise NoChatLoaded
        return self._messages_df

    @messages_df.setter
    def messages_df(self, messages_df: pd.DataFrame):
        self._messages_df = messages_df

    def unset_participant(self) -> None:

        self._current_participant = None

    def set_participant(self, participant: str) -> None:
        if participant not in self.participants():
            raise ValueError("Unknown participant name.")

        self._current_participant = participant

    def total_messages(
        self, date: Optional[str] = None, participant: Optional[str] = None
    ) -> int:
        """Return the number of messages in the current chat."""
        if participant is None and self._current_participant is not None:
            participant = self._current_participant

        if date is None and participant is None:
            messages: int = len(self.messages_df)
            return messages
        elif date and not participant:
            mask = self.messages_df["Date"].str.startswith(date)
            return mask.sum()
        elif participant and not date:
            mask = self.messages_df["Sender"] == participant
            return mask.sum()
        else:
            mask = (self.messages_df["Date"].str.startswith(date)) & (
                self.messages_df["Sender"] == participant
            )
            return mask.sum()

    def participants(self) -> list[str]:
        """Return a list with the name of every participant."""

        participants: list[str] = sorted(self.messages_df["Sender"].unique())

        return participants

    def messages_per_participant(self, date: Optional[str] = None) -> dict[str, int]:
        """Return the quantity of messages per participant.

        Args:
            date (Optional[str]): The date in format (YY-MM-DD),can also be (YY-MM) for getting the messages in a month or in a year (YY).
        Returns:
            dict[str, int]

        """

        # No date specified
        if date is None:
            return self.messages_df["Sender"].value_counts().to_dict()

        # Date specified
        mask = self.messages_df["Date"] == date
        return self.messages_df[mask].value_counts().to_dict()
