from typing import Optional

import numpy as np

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit
from PyQt6.QtCore import Qt

from src.core.analizer import Analizer
from src.ui.charts.charts import Charts
from src.models.constants import months_dict


analizer = Analizer()


class YearTab(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.charts: Optional[Charts] = None

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.setSpacing(20)
        self.layout.setContentsMargins(20, 20, 20, 20)

        self.year = QLineEdit()
        self.year.setPlaceholderText("Year...")
        self.year.setObjectName("date_input")

        self.year.editingFinished.connect(self.load)

        self.layout.addWidget(self.year, alignment=Qt.AlignmentFlag.AlignCenter)

        self.space = QWidget(self)
        self.layout.addWidget(self.space)

    def load(self):

        year = self.year.text()

        if not year:
            return

        if isinstance(self.charts, Charts):
            self.charts.hide()

        months = list(months_dict.keys())

        self.space.hide()

        months_array = np.arange(1, 13)

        messages = analizer.total_messages(date=year, iterate=(1, 12))

        mess_array = np.array(messages)

        self.charts = Charts(
            title=year,
            axis=(months_array, mess_array),
            lin_labels=("Months", "Messages"),
            sq_index=months,
            sq_size=6,
        )

        self.layout.addWidget(self.charts)
