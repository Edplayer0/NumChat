"""Analizer module that provides methods to analyze the chat data."""

from typing import Optional

import pandas as pd

from src.models.exceptions import NoChatLoaded


class Analizer:
    """Singleton class that provides methods to analyze the chat data."""

    def __new__(cls) -> "Analizer":
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._current_participant: Optional[str] = None
        self._cache = {}

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
        # Reset cache when new data is loaded
        self._cache.clear()
        # Set indices for faster lookups
        self._messages_df.set_index(
            ["Date", "Time", "Sender"], inplace=True, drop=False
        )

    def unset_participant(self) -> None:

        self._current_participant = None

    def set_participant(self, participant: str) -> None:
        if participant not in self.participants():
            raise ValueError("Unknown participant name.")

        self._current_participant = participant

    def total_messages(
        self,
        date: Optional[str] = None,
        participant: Optional[str] = None,
        time: Optional[str] = None,
    ) -> int:
        """Return the number of messages in the current chat."""
        if participant is None and self._current_participant is not None:
            participant = self._current_participant

        cache_key = (date, participant, time)
        if cache_key in self._cache:
            return self._cache[cache_key]

        query = {}
        if date:
            query["Date"] = date
        if time:
            query["Time"] = time
        if participant:
            query["Sender"] = participant

        filtered_df = self.messages_df
        for key, value in query.items():
            filtered_df = filtered_df[filtered_df[key].str.startswith(value)]

        result = len(filtered_df)
        self._cache[cache_key] = result
        return result

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

        if date is None:
            result = self.messages_df["Sender"].value_counts().to_dict()
        else:
            result = (
                self.messages_df[self.messages_df["Date"].str.startswith(date)][
                    "Sender"
                ]
                .value_counts()
                .to_dict()
            )

        return result
