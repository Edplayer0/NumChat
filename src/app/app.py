import sys

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QApplication


class App(QApplication):
    def __init__(self):
        super().__init__(sys.argv)

        self.setApplicationName("NumChat: Chat Analizer")

    def mainloop(self):
        """Enter in the application loop"""

        sys.exit(self.exec())
