from typing import Optional

import pandas as pd

from src.models.exceptions import NoChatLoaded


class Analizer:

    def __new__(cls) -> "Analizer":
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

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

    def total_messages(self, date: Optional[str] = None) -> int:
        """Return the number of messages in the current chat."""

        if not date:
            messages: int = len(self.messages_df)

            return messages

        messages = self.messages_df["Date"].str.startswith(date)
        return messages.sum()

    def participants(self) -> list[str]:
        """Return a list with the name of every participant."""

        participants: list[str] = sorted(self.messages_df["Sender"].unique())

        return participants

    def messages_per_participant(
        self, date: Optional[str] = None, participant: Optional[str] = None
    ) -> dict[str, int] | int:
        """Return the quantity of messages per participant.

        Args:
            date (Optional[str]): The date in format (YY-MM-DD),
            can also be (YY-MM) for getting the messages in a month or in a year (YY).
            participant (Optional[str]): Can be selected an specific participant.
        Returns:
            dict[str, int]: if there is more than one participant selected (by default).
            int: if you specify a single participant.

        """

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
