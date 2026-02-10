from typing import Optional

from numpy import ndarray

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QFormLayout,
    QGroupBox,
)
from PyQt6.QtCore import Qt


class SquareChart(QWidget):
    def __init__(
        self,
        data: ndarray,
        *args,
        label: Optional[str] = None,
        width: int = 7,
        index: Optional[list] = None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        class Info(QGroupBox):
            def __init__(self, data: ndarray, *args, **kwargs):
                super().__init__(*args, **kwargs)

                layout = QFormLayout()
                self.setLayout(layout)

                self.setTitle("Details")

                layout.setSpacing(5)

                highest_value = data.max()
                minimun_value = data.min()
                mean = round(data.mean())
                total = data.sum()

                minumun = QLabel(text=f"Minimun:  {minimun_value}", parent=self)
                highest = QLabel(text=f"Highest:  {highest_value}", parent=self)
                mean_label = QLabel(text=f"Promedy:  {mean}", parent=self)
                total_label = QLabel(text=f"Total:  {total}", parent=self)
                layout.addWidget(minumun)
                layout.addWidget(highest)
                layout.addWidget(mean_label)
                layout.addWidget(total_label)

                self.setStyleSheet(
                    """QGroupBox {font-size: 16px; font-weight: bold;}
                    QLabel {font-size: 14px;}
                """
                )

        class Line(QWidget):
            def __init__(
                self, data, mean, *args, index: Optional[list] = None, **kwargs
            ):
                super().__init__(*args, **kwargs)

                class Square(QWidget):
                    def __init__(
                        self,
                        color: str,
                        *args,
                        text: str = "",
                        value: Optional[int] = None,
                        **kwargs,
                    ):
                        super().__init__(*args, **kwargs)

                        layout = QVBoxLayout()
                        self.setLayout(layout)
                        layout.setContentsMargins(0, 0, 0, 0)

                        square = QPushButton(text=str(text), parent=self)
                        style = (
                            """QPushButton {
                        border-radius: 10px;
                        background-color: """
                            + color
                            + """;
                        width: 45px;
                        height: 45px;
                        }"""
                        )
                        square.setStyleSheet(style)

                        layout.addWidget(square)

                        if value is not None:
                            value_label = QLabel(text=str(value), parent=self)
                            layout.addWidget(
                                value_label, alignment=Qt.AlignmentFlag.AlignCenter
                            )

                layout = QHBoxLayout()
                self.setLayout(layout)

                layout.setSpacing(6)
                layout.setContentsMargins(0, 0, 0, 0)

                for idx, value in zip(index, data):

                    if value == 0:
                        color = "rgb(200, 200, 200)"
                    elif value < mean * 0.25:
                        color = "rgb(178, 237, 255)"
                    elif value < mean * 0.75:
                        color = "rgb(136, 223, 255)"
                    elif value < mean * 1.25:
                        color = "#66a1f8"
                    elif value < mean * 1.50:
                        color = "#0d6efd"
                    else:
                        color = "blue"

                    square = Square(color, text=idx, value=value)

                    layout.addWidget(square)

        if index is None:
            index = list(range(1, len(data) + 1))

        layout = QVBoxLayout()
        self.setLayout(layout)

        mean = data.mean()

        graph = QHBoxLayout()

        lines = QVBoxLayout()
        lines.setSpacing(6)

        if label is not None:
            qlabel = QLabel(text=label, parent=self)
            qlabel.setStyleSheet(
                """QLabel {
            font-size: 13px;
            font: Segoe UI;
            }"""
            )
            lines.addWidget(qlabel, alignment=Qt.AlignmentFlag.AlignCenter)

        for idx in range(0, len(data), width):
            sliced = data[idx : idx + width]
            line = Line(sliced, mean, index=index[idx : width + idx], parent=self)
            lines.addWidget(line)

        info = Info(data, parent=self)
        graph.addLayout(lines)
        graph.addWidget(info, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addLayout(graph)
