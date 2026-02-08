from typing import Optional

import numpy as np

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt6.QtCore import Qt

from src.core.analizer import Analizer
from src.ui.charts.square_chart import SquareChart
from src.ui.charts.linear_chart import LinearChart
from src.models.constants import months_dict


analizer = Analizer()


class YearTab(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sq_chart: Optional[SquareChart] = None
        self.linear_chart: Optional[LinearChart] = None

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

        if isinstance(self.sq_chart, SquareChart):
            self.sq_chart.hide()
            self.linear_chart.hide()

        months = list(months_dict.keys())

        self.space.hide()

        year = self.year.text()

        messages: list[int] = []

        months_array = np.arange(1, 13)

        for month in months_array:
            month = str(month)
            mes_quantity = analizer.total_messages(f"{year}-{month.rjust(2, "0")}")
            messages.append(mes_quantity)

        mess_array = np.array(messages)

        charts = QHBoxLayout()

        self.sq_chart = SquareChart(mess_array, label=year, width=6, index=months)

        self.linear_chart = LinearChart()
        self.linear_chart.axes.plot(months_array, mess_array)
        self.linear_chart.axes.set_title(year)
        self.linear_chart.axes.set_xlabel("Months")
        self.linear_chart.axes.set_ylabel("Messages")
        self.linear_chart.axes.grid(True)

        charts.addWidget(self.sq_chart, alignment=Qt.AlignmentFlag.AlignCenter)
        charts.addWidget(self.linear_chart, alignment=Qt.AlignmentFlag.AlignCenter)

        self.layout.addLayout(charts)
