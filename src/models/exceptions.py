"""Custom exceptions module."""


class NoChatLoaded(Exception):
    """No chat have been loaded yet."""

    def __init__(self, message="No chat have been loaded yet."):

        super().__init__(message)


class UnknownChatFormat(Exception):
    """Unknown chat format, likely due to an unsopported platform."""

    def __init__(
        self, message="Unknown chat format, likely due to an unsopported platform."
    ):

        super().__init__(message)
