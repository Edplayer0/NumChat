from typing import Optional

import numpy as np

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QHBoxLayout
from PyQt6.QtCore import Qt

from src.core.analizer import Analizer
from src.ui.charts.charts import Charts
from src.models.constants import months_dict

analizer = Analizer()


class MonthTab(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.charts: Optional[Charts] = None

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.setSpacing(20)
        self.layout.setContentsMargins(20, 20, 20, 20)

        form = QWidget(self)
        form_layout = QHBoxLayout()
        form.setLayout(form_layout)

        self.year = QLineEdit(form)
        self.year.setPlaceholderText("Year.. .")
        self.year.setObjectName("date_input")
        self.month = QLineEdit(form)
        self.month.setPlaceholderText("Month.. .")
        self.month.setObjectName("date_input")

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

        if isinstance(self.charts, Charts):
            self.charts.hide()
            del self.charts

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

        self.charts = Charts(
            title=f"{year}-{month}",
            axis=(days_array, mess_array),
            lin_labels=("Days", "Messages"),
            sq_size=8,
            parent=self,
        )

        self.layout.addWidget(self.charts)
