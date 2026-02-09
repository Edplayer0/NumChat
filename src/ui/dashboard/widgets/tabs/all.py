from typing import Optional

import numpy as np

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from matplotlib.ticker import MaxNLocator

from src.core.analizer import Analizer
from src.ui.charts.linear_chart import LinearChart

analizer = Analizer()


class AllTab(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.chart: Optional[LinearChart] = None

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.dates = analizer.messages_df["Date"].unique()
        self.load()

    def load(self):

        if isinstance(self.chart, LinearChart):
            self.chart.hide()

        messages = []

        for _, date in enumerate(self.dates):
            mess = analizer.total_messages(date=date)
            messages.append(mess)

        mess_array = np.array(messages)

        self.chart = LinearChart(
            data=(self.dates, mess_array),
            labels=("Time", "Messages"),
            title="All chat history",
            width=10,
            height=7,
        )
        self.chart.axes.xaxis.set_major_locator(MaxNLocator(8))
        self.layout.addWidget(self.chart, alignment=Qt.AlignmentFlag.AlignCenter)
