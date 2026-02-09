from typing import Optional

import numpy as np

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QHBoxLayout
from PyQt6.QtCore import Qt

from src.core.analizer import Analizer
from src.ui.charts.charts import Charts

analizer = Analizer()


class DayTab(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.charts: Optional[QWidget] = None

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.setSpacing(20)
        self.layout.setContentsMargins(20, 20, 20, 20)

        form = QWidget(self)
        form_layout = QHBoxLayout()
        form.setLayout(form_layout)

        self.day = QLineEdit(form)
        self.day.setPlaceholderText("Day...")
        self.day.setObjectName("date_input")
        self.month = QLineEdit(form)
        self.month.setPlaceholderText("Month...")
        self.month.setObjectName("date_input")
        self.year = QLineEdit(form)
        self.year.setPlaceholderText("Year...")
        self.year.setObjectName("date_input")

        self.day.editingFinished.connect(self.load)
        self.month.editingFinished.connect(self.load)
        self.year.editingFinished.connect(self.load)

        form_layout.addWidget(self.day)
        form_layout.addWidget(self.month)
        form_layout.addWidget(self.year)

        self.layout.addWidget(form, alignment=Qt.AlignmentFlag.AlignCenter)

        self.space = QWidget(self)
        self.layout.addWidget(self.space)

    def load(self):

        day = self.day.text().rjust(2, "0")
        month = self.month.text().rjust(2, "0")
        year = self.year.text()

        if not all((day, month, year)):
            return

        if isinstance(self.charts, Charts):
            self.charts.hide()
            del self.charts

        self.space.hide()

        messages: list[int] = []

        hours_array = np.arange(24)

        for hour in hours_array:
            hour = str(hour).rjust(2, "0") + ":"
            date = f"{year}-{month}-{day}"
            mes_quantity = analizer.total_messages(date=date, time=hour)
            messages.append(mes_quantity)

        if not messages:
            return

        mess_array = np.array(messages)

        self.charts = Charts(
            title=f"{year}-{month}-{day}",
            axis=(hours_array, mess_array),
            lin_labels=("Hours", "Messages"),
            sq_index=list(hours_array),
        )

        self.layout.addWidget(self.charts)
