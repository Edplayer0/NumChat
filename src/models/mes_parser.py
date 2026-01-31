from abc import ABC, abstractmethod


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
