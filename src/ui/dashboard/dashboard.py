# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QHBoxLayout

from src.ui.dashboard.widgets.control_panel import ControlPanel
from src.ui.dashboard.widgets.tab_widget import TabWidget


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.tabs = TabWidget(self)

        # instanciating ControlPanel starts loading the AllTab
        control_panel = ControlPanel(self)

        layout.addWidget(control_panel)
        layout.addWidget(self.tabs)
