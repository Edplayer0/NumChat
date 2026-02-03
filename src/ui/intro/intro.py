import sys

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QHBoxLayout
from PyQt6.QtCore import Qt

from src.core.controller import Controller


class Intro(QWidget):

    def __init__(self, controller: Controller, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout(self)

        self.setLayout(layout)

        heading = QLabel("Welcome", self, alignment=Qt.AlignmentFlag.AlignCenter)
        heading.setObjectName("heading")

        subheading = QLabel(
            " Select a JSON file with an exported chat",
            self,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )
        subheading.setObjectName("subheading")

        explore_button = QPushButton("Explore", self)
        explore_button.setObjectName("explore")
        explore_button.clicked.connect(lambda: controller.start())

        cancel_button = QPushButton("Cancel", self)
        cancel_button.setObjectName("cancel")
        cancel_button.clicked.connect(sys.exit)

        buttons = QHBoxLayout()

        buttons.setContentsMargins(50, 50, 50, 50)
        buttons.setSpacing(50)

        buttons.addWidget(explore_button)
        buttons.addWidget(cancel_button)

        layout.addWidget(heading)
        layout.addWidget(subheading)
        layout.addLayout(buttons)
