# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

from src.core.analizer import Analizer

analizer = Analizer()


class ControlPanel(QWidget):
    def __init__(self, *args):
        super().__init__(*args)

        class Info(QWidget):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

                layout = QVBoxLayout()
                self.setLayout(layout)

                layout.setContentsMargins(0, 0, 0, 0)

                general = QLabel(text="General info", parent=self)
                platform = QLabel(text="Platform: Telegram", parent=self)

                start = analizer.messages_df.iloc[0, 0]
                end = analizer.messages_df.iloc[-1, 0]

                start_label = QLabel(text=f"Start: {start}", parent=self)
                end_label = QLabel(text=f"End: {end}", parent=self)

                layout.addWidget(general, alignment=Qt.AlignmentFlag.AlignCenter)
                layout.addWidget(platform, alignment=Qt.AlignmentFlag.AlignCenter)
                layout.addWidget(start_label, alignment=Qt.AlignmentFlag.AlignCenter)
                layout.addWidget(end_label, alignment=Qt.AlignmentFlag.AlignCenter)

                self.setStyleSheet("QLabel {font-size: 15px}")
                general.setStyleSheet("QLabel {font-weight: bold; font-size: 17px}")

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.setContentsMargins(0, 0, 0, 0)

        label = QLabel("Chat Analizer", self, alignment=Qt.AlignmentFlag.AlignTop)
        label.setObjectName("label")

        layout.addWidget(label)

        info = Info(parent=self)
        layout.addWidget(info, alignment=Qt.AlignmentFlag.AlignCenter)

        buttons = QWidget(self)

        buttons_layout = QVBoxLayout()
        buttons.setLayout(buttons_layout)

        buttons_layout.setSpacing(0)
        buttons_layout.setContentsMargins(0, 0, 0, 0)

        mess_per_participants = analizer.messages_per_participant()

        self.buttons = []

        for participant in mess_per_participants.items():
            par_button = QPushButton(
                text=f" {participant[0]}: {participant[1]}", parent=buttons
            )
            self.buttons.append(par_button)
            buttons_layout.addWidget(par_button)

        total = QPushButton(
            text=" Total: " + str(analizer.total_messages()), parent=buttons
        )
        self.buttons.append(total)
        self.activate(total)

        buttons_layout.addWidget(total)

        layout.addWidget(buttons, alignment=Qt.AlignmentFlag.AlignBottom)

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
