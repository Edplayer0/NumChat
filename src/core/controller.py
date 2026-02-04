# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QFileDialog

from src.models.parser import MessagesParser

from src.core.parsers import TelegramParser
from src.core.analizer import Analizer

from src.models.exceptions import UnknownChatFormat


class Controller:

    def __init__(self):
        self.window = None

    def _new_file(self) -> str:
        """Open a file dialog to select the file"""
        file_path, _ = QFileDialog.getOpenFileName(
            filter="*.json", caption="Select an exported chat"
        )
        return file_path

    def _choose_parser(self, file_path: str) -> MessagesParser:

        if True:
            return TelegramParser()

        raise UnknownChatFormat

    def start(self):
        """Start the file selection and parser selection"""
        file_path = self._new_file()

        if not file_path.strip():
            return

        parser: MessagesParser = self._choose_parser(file_path)

        try:
            df = parser.load_messages(file_path)
        except Exception as exc:
            raise UnknownChatFormat from exc

        # Initializing the analizer
        Analizer().messages_df = df

        self.window.start_dashboard()
