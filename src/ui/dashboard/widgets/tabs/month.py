from typing import Optional

import numpy as np

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QHBoxLayout
from PyQt6.QtCore import Qt

from src.core.analizer import Analizer
from src.ui.charts.square_chart import SquareChart
from src.ui.charts.linear_chart import LinearChart
from src.models.constants import months_dict

analizer = Analizer()


class MonthTab(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sq_chart: Optional[SquareChart] = None
        self.linear_chart: Optional[LinearChart] = None

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.setSpacing(20)
        self.layout.setContentsMargins(20, 20, 20, 20)

        form = QWidget(self)
        form_layout = QHBoxLayout()
        form.setLayout(form_layout)

        self.year = QLineEdit(form)
        self.year.setPlaceholderText("Year.. .")
        self.year.setObjectName("year_input")
        self.month = QLineEdit(form)
        self.month.setPlaceholderText("Month.. .")
        self.month.setObjectName("year_input")

        self.month.editingFinished.connect(self.load)
        self.year.editingFinished.connect(self.load)

        form_layout.addWidget(self.month)
        form_layout.addWidget(self.year)

        self.layout.addWidget(form, alignment=Qt.AlignmentFlag.AlignCenter)

        self.space = QWidget(self)
        self.layout.addWidget(self.space)

    def load(self):

        month = self.month.text().rjust(2, "0")
        year = self.year.text()

        if not all((month, year)):
            return

        if isinstance(self.sq_chart, SquareChart):
            self.sq_chart.hide()
            self.linear_chart.hide()

        self.space.hide()

        messages: list[int] = []

        days = list(months_dict.values())[int(month) - 1]

        days_array = np.arange(1, days + 1)

        for day in days_array:
            day = str(day)
            date = f"{year}-{month}-{day.rjust(2, "0")}"
            mes_quantity = analizer.total_messages(date=date)
            messages.append(mes_quantity)

        mess_array = np.array(messages)

        self.sq_chart = SquareChart(mess_array, label=f"{year}-{month}", width=8)

        charts = QHBoxLayout()

        self.linear_chart = LinearChart(
            data=(days_array, mess_array),
            title=f"{year}-{month}",
            labels=("Days", "Messages"),
        )

        charts.addWidget(self.sq_chart, alignment=Qt.AlignmentFlag.AlignCenter)
        charts.addWidget(self.linear_chart, alignment=Qt.AlignmentFlag.AlignCenter)

        self.layout.addLayout(charts)
