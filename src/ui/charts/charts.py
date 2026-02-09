from typing import Optional

from numpy import ndarray

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QHBoxLayout
from PyQt6.QtCore import Qt

from src.ui.charts.square_chart import SquareChart
from src.ui.charts.linear_chart import LinearChart


class Charts(QWidget):
    def __init__(
        self,
        title: str,
        axis: tuple[ndarray, ndarray],
        *args,
        sq_index: Optional[list] = None,
        sq_size: int = 7,
        lin_labels: tuple[str, str] = None,
        **kwargs
    ):
        super().__init__(*args, **kwargs)

        layout = QHBoxLayout()
        self.setLayout(layout)

        sq_chart = SquareChart(data=axis[1], label=title, index=sq_index, width=sq_size)
        linear_chart = LinearChart(data=axis, title=title, labels=lin_labels)

        layout.addWidget(sq_chart, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(linear_chart, alignment=Qt.AlignmentFlag.AlignCenter)
