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

    def load(self):

        if isinstance(self.chart, LinearChart):
            self.chart.hide()

        messages = []

        # Reduce the number of points if there are too many dates
        max_points = 100
        if len(self.dates) > max_points:
            step = len(self.dates) // max_points
            reduced_dates = self.dates[::step]
        else:
            reduced_dates = self.dates

        for date in reduced_dates:
            mess = analizer.total_messages(date=date)
            messages.append(mess)

        mess_array = np.array(messages)

        self.chart = LinearChart(
            data=(reduced_dates, mess_array),
            labels=("Time", "Messages"),
            title="All chat history",
            width=10,
            height=7,
        )
        self.chart.axes.xaxis.set_major_locator(MaxNLocator(8))
        self.layout.addWidget(self.chart, alignment=Qt.AlignmentFlag.AlignCenter)
