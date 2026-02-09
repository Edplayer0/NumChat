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

        layout = QVBoxLayout()
        self.setLayout(layout)

        dates = analizer.messages_df["Date"].unique()

        messages = []

        for _, date in enumerate(dates):
            mess = analizer.total_messages(date=date)
            messages.append(mess)

        mess_array = np.array(messages)

        chart = LinearChart(
            data=(dates, mess_array),
            labels=("Time", "Messages"),
            title="All history",
            width=10,
            height=7,
        )
        chart.axes.xaxis.set_major_locator(MaxNLocator(8))
        layout.addWidget(chart, alignment=Qt.AlignmentFlag.AlignCenter)
