# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QHBoxLayout

from src.ui.dashboard.widgets.control_panel import ControlPanel
from src.ui.dashboard.widgets.tab_widget import TabWidget


class Dashboard(QWidget):
    def __init__(self, parser):
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        control_panel = ControlPanel(parser, self)
        layout.addWidget(control_panel)

        tabs = TabWidget(parser, self)
        layout.addWidget(tabs)
