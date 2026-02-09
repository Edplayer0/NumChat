# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QTabWidget

from src.ui.dashboard.widgets.tabs.year import YearTab
from src.ui.dashboard.widgets.tabs.month import MonthTab
from src.ui.dashboard.widgets.tabs.week import WeekTab
from src.ui.dashboard.widgets.tabs.all import AllTab


class TabWidget(QTabWidget):
    def __init__(self, *args):
        super().__init__(*args)

        self.tabs = {
            "Week": WeekTab(self),
            "Month": MonthTab(self),
            "Year": YearTab(self),
            "All": AllTab(self),
        }

        for name, widget in self.tabs.items():
            self.addTab(widget, name)

        self.setObjectName("tab")

    def reload(self):
        for tab in self.tabs.values():
            tab.load()
