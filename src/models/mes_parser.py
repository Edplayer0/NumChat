from abc import ABC, abstractmethod

from typing import Optional


class MessagesParser(ABC):

    @abstractmethod
    def load_messages(self):
        """Load the messages from an exported file."""

    @abstractmethod
    def total_messages(self) -> int:
        """Return the number of messages in the loaded chat."""

    @abstractmethod
    def participants(self) -> list[str]:
        """Return the a list with participants's name."""

    @abstractmethod
    def messages_per_participant(
        self, date: Optional[str], participant: Optional[str]
    ) -> dict[str, int] | int:
        """Return the numbers of messages per participant
        allowing you to specify certain participant and/or date."""
