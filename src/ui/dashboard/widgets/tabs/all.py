from typing import Optional

import numpy as np

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from matplotlib.ticker import MaxNLocator

from src.core.analizer import Analizer
from src.ui.charts.linear_chart import LinearChart
from src.models.constants import months_dict

analizer = Analizer()


class AllTab(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.chart: Optional[LinearChart] = None

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.dates = analizer.messages_df["Date"].unique().tolist()

    def load(self):

        if isinstance(self.chart, LinearChart):
            self.chart.hide()

        messages = []

        # Reduce the number of points if there are too many dates
        max_points = 100
        step = len(self.dates) // max_points
        dates = self.dates[::step]

        if step >= 3:

            if not self.dates[-1] in dates:
                dates.append(self.dates[-1])

            months = list(months_dict.values())

            step //= 2

            for date in dates:
                day = int(date[-2:])
                month = int(date[5:7])
                date = date[:-3]

                start = max(day - step, 1)
                end = min(day + step, months[month - 1])

                days_mess = np.array(
                    analizer.total_messages(date=date, iterate=(start, end + 1))
                )
                messages.append(days_mess.mean())

        elif step > 1:

            for date in dates:
                mess = analizer.total_messages(date=date)
                messages.append(mess)

        else:
            for date in self.dates:
                mess = analizer.total_messages(date=date)
                messages.append(mess)

        mess_array = np.array(messages)

        self.chart = LinearChart(
            data=(dates, mess_array),
            labels=("Time", "Messages"),
            title="All chat history",
            width=10,
            height=7,
        )
        self.chart.axes.xaxis.set_major_locator(MaxNLocator(8))
        self.layout.addWidget(self.chart, alignment=Qt.AlignmentFlag.AlignCenter)
