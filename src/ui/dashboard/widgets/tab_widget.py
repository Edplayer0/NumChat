# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QTabWidget

from src.models.mes_parser import MessagesParser


class TabWidget(QTabWidget):
    def __init__(self, parser: MessagesParser, parent):
        super().__init__(parent=parent)

        self.addTab(QWidget(self), "Week")
        self.addTab(QWidget(self), "Month")
        self.addTab(QWidget(self), "Year")
        self.addTab(QWidget(self), "All")
