# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QTabWidget


class TabWidget(QTabWidget):
    def __init__(self, *args):
        super().__init__(*args)

        self.addTab(QWidget(self), "Week")
        self.addTab(QWidget(self), "Month")
        self.addTab(QWidget(self), "Year")
        self.addTab(QWidget(self), "All")

        self.setObjectName("tab")
