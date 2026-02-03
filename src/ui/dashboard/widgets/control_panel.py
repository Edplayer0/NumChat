# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

from src.models.mes_parser import MessagesParser


class ControlPanel(QWidget):
    def __init__(self, parser: MessagesParser, parent):
        super().__init__(parent=parent)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.setContentsMargins(0, 0, 0, 0)

        label = QLabel("Chat Analizer", self, alignment=Qt.AlignmentFlag.AlignTop)
        label.setObjectName("label")

        layout.addWidget(label)

        layout.addStretch()

        info = QWidget(self)
        info.setObjectName("info")

        info_layout = QVBoxLayout()
        info.setLayout(info_layout)

        mess_per_participants = parser.messages_per_participant()

        for participant in mess_per_participants.items():
            par_label = QLabel(f" {participant[0]}: {participant[1]}", info)
            par_label.setObjectName("participant")
            info_layout.addWidget(par_label)

        total = QLabel(" Total: " + str(parser.total_messages()), info)
        total.setObjectName("participant")

        info_layout.addWidget(total)

        layout.addWidget(info)
