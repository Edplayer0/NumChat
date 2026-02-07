from typing import Optional

import numpy as np

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit
from PyQt6.QtCore import Qt

from src.core.analizer import Analizer
from src.ui.dashboard.widgets.charts.square_chart import SquareChart
from src.models.constants import months_dict


analizer = Analizer()


class YearTab(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sq_chart: Optional[QWidget] = None

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.setSpacing(20)
        self.layout.setContentsMargins(20, 20, 20, 20)

        self.year = QLineEdit()
        self.year.setPlaceholderText("Year...")
        self.year.setObjectName("year_input")

        self.year.editingFinished.connect(self.load)

        self.layout.addWidget(self.year, alignment=Qt.AlignmentFlag.AlignCenter)

        self.space = QWidget(self)
        self.layout.addWidget(self.space)

    def load(self):

        if isinstance(self.sq_chart, QWidget):
            self.sq_chart.hide()

        months = list(months_dict.keys())

        self.space.hide()

        year = self.year.text()

        messages: list[int] = []

        for month in range(1, 13):
            month = str(month)
            mes_quantity = analizer.total_messages(f"{year}-{month.rjust(2, "0")}")
            messages.append(mes_quantity)

        mess_array = np.array(messages)

        self.sq_chart = SquareChart(mess_array, label=year, width=6, index=months)

        self.layout.addWidget(self.sq_chart, alignment=Qt.AlignmentFlag.AlignCenter)
