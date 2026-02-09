# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QTabWidget

from src.ui.dashboard.widgets.tabs.year import YearTab
from src.ui.dashboard.widgets.tabs.month import MonthTab
from src.ui.dashboard.widgets.tabs.week import WeekTab
from src.ui.dashboard.widgets.tabs.all import AllTab


class TabWidget(QTabWidget):
    def __init__(self, *args):
        super().__init__(*args)

        self.addTab(WeekTab(self), "Week")
        self.addTab(MonthTab(self), "Month")
        self.addTab(YearTab(self), "Year")
        self.addTab(AllTab(self), "All")

        self.setObjectName("tab")
