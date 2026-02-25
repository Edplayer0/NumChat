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

        # Groups for faster lookups
        self.grouped_by_date = self._messages_df.groupby("Date").size().to_dict()
        self.grouped_by_date_and_participant = (
            self._messages_df.groupby(by=["Date", "Sender"]).size().to_dict()
        )

    def unset_participant(self) -> None:
        """Unset the current participant,
        so the total_messages method will return the total messages of all participants.
        """

        self._current_participant = None

    def set_participant(self, participant: str) -> None:
        """Set the current participant,
        so the total_messages method will return the total messages of that participant.
        """
        if participant not in self.participants():
            raise ValueError("Unknown participant name.")

        self._current_participant = participant

    def total_messages(
        self,
        date: Optional[str] = None,
        time: Optional[str] = None,
        iterate: Optional[tuple[int, int]] = None,
    ) -> int | list[int]:
        """Return the total number of messages in the current chat, filtered by date, time and participant.

        Args:
            date (Optional[str]): The date in format (YY-MM-DD),can also be (YY-MM) for getting the messages in a month or in a year (YY).
            time (Optional[str]): The time in format (HH).
            iterate (Optional[tuple[int, int]]): A tuple with the start and end of the iteration, used for getting the messages in a range of dates or times.
        Returns:
            int | list[int]: The number of messages in the current chat, or a list with the number of messages in a range of dates or times.

        """

        # Set the participant
        participant = self._current_participant

        # Generate a cache_key and search for cached results
        cache_key = (date, participant, time, iterate)
        if cache_key in self._cache:
            return self._cache[cache_key]

        # Iterate over the next level of uncomplete date or time
        if iterate and date:

            if len(date) < 10:
                target = date
            else:
                target = time

            start = iterate[0]
            end = iterate[1] + 1

            if target == date:
                values = [
                    self.total_messages(date=f"{date}-{str(var).rjust(2, '0')}")
                    for var in range(start, end)
                ]
            else:
                values = [
                    self.total_messages(date=date, time=str(var).rjust(2, "0"))
                    for var in range(start, end)
                ]

            self._cache[cache_key] = values

            return values

        # When an specific date is provided, uses the grouped dataframes
        # for faster lookups
        if date is not None and len(date) == 10 and time is None:
            if participant is None:
                return self.grouped_by_date.get(date, 0)

            return self.grouped_by_date_and_participant.get((date, participant), 0)

        # Generate a query when isn't provided an specific date or time
        query = []
        if date:
            query.append(f"Date.str.startswith('{date}')")
        if time:
            query.append(f"Time.str.startswith('{time}')")
        if participant:
            query.append(f"Sender == '{participant}'")

        # Filter the dataframe
        if query:
            filtered_df = self.messages_df.query(" and ".join(query))
        else:
            filtered_df = self.messages_df

        result = len(filtered_df)

        # Cache the result
        self._cache[cache_key] = result

        return result

    def participants(self) -> list[str]:
        """Return a list with the name of every participant."""

        participants: list[str] = sorted(self.messages_df["Sender"].unique())

        return participants

    def messages_per_participant(self) -> dict[str, int]:
        """Return the quantity of messages per participant."""

        result = self.messages_df["Sender"].value_counts().to_dict()

        return result
