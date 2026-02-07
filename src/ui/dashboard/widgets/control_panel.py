# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

from src.core.analizer import Analizer


class ControlPanel(QWidget):
    def __init__(self, *args):
        super().__init__(*args)

        self.analizer = Analizer()

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.setContentsMargins(0, 0, 0, 0)

        label = QLabel("Chat Analizer", self, alignment=Qt.AlignmentFlag.AlignTop)
        label.setObjectName("label")

        layout.addWidget(label)

        layout.addStretch()

        info = QWidget(self)

        info_layout = QVBoxLayout()
        info.setLayout(info_layout)

        info_layout.setSpacing(0)
        info_layout.setContentsMargins(0, 0, 0, 0)

        mess_per_participants = self.analizer.messages_per_participant()

        self.buttons = []

        for participant in mess_per_participants.items():
            par_button = QPushButton(
                text=f" {participant[0]}: {participant[1]}", parent=info
            )
            self.buttons.append(par_button)
            info_layout.addWidget(par_button)

        total = QPushButton(
            text=" Total: " + str(self.analizer.total_messages()), parent=info
        )
        self.buttons.append(total)
        self.activate(total)

        info_layout.addWidget(total)

        layout.addWidget(info)

    def activate(self, button: QPushButton) -> None:
        button.setStyleSheet(
            """QPushButton {
    font-size: 18px;
    font: Segoe UI Symbol;
    border: 0 solid black;
    background: rgb(136, 223, 255);
    text-align: left;
    padding: 9px;
    color: black;
    border-radius: 0px;
}"""
        )

        other_buttons = self.buttons.copy()
        other_buttons.remove(button)

        for other_button in other_buttons:
            self.deactivate(other_button)

        try:
            button.clicked.disconnect()
        except TypeError:
            pass

    def deactivate(self, button: QPushButton) -> None:
        button.setStyleSheet(
            """QPushButton {
    font-size: 18px;
    font: Segoe UI Symbol;
    background: white;
    border: 0 solid black;
    text-align: left;
    padding: 9px;
    color: black;
    border-radius: 0px;
}
QPushButton:hover {
    font-size: 18px;
    font: Segoe UI Symbol;
    border: 0 solid black;
    background: rgb(178, 237, 255);
    text-align: left;
    padding: 9px;
    color: black;
    border-radius: 0px;
}"""
        )

        try:
            button.clicked.disconnect()
        except TypeError:
            pass

        button.clicked.connect(lambda: self.activate(button))
