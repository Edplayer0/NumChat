from typing import Optional

import numpy as np

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QHBoxLayout
from PyQt6.QtCore import Qt

from src.core.analizer import Analizer
from src.ui.charts.square_chart import SquareChart
from src.models.constants import months_dict

analizer = Analizer()


class MonthTab(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sq_chart: Optional[QWidget] = None

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

        month = self.month.text()
        year = self.year.text()

        if not all((month, year)):
            return

        if isinstance(self.sq_chart, QWidget):
            self.sq_chart.hide()

        self.space.hide()

        messages: list[int] = []

        days = list(months_dict.values())[int(month) - 1]

        for day in range(1, days + 1):
            day = str(day)
            date = f"{year}-{month.rjust(2, "0")}-{day.rjust(2, "0")}"
            mes_quantity = analizer.total_messages(date=date)
            messages.append(mes_quantity)

        mess_array = np.array(messages)

        self.sq_chart = SquareChart(
            mess_array, label=f"{year}-{month.rjust(2, "0")}", width=8
        )

        self.layout.addWidget(self.sq_chart, alignment=Qt.AlignmentFlag.AlignCenter)
