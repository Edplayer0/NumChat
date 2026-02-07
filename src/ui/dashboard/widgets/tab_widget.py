# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QTabWidget

from src.ui.dashboard.widgets.tabs.year import YearTab
from src.ui.dashboard.widgets.tabs.month import MonthTab


class TabWidget(QTabWidget):
    def __init__(self, *args):
        super().__init__(*args)

        self.addTab(QWidget(self), "Week")
        self.addTab(MonthTab(self), "Month")
        self.addTab(YearTab(self), "Year")
        self.addTab(QWidget(self), "All")

        self.setObjectName("tab")
