import sys

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

from src.core.controller import Controller


class Intro(QWidget):

    def __init__(self, controller: Controller, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout(self)

        layout.setSpacing(20)
        layout.setContentsMargins(20, 0, 20, 5)

        self.setLayout(layout)

        pixmap = QIcon("assets/icon.ico").pixmap(100, 100)

        logo = QLabel(self)
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
        buttons.setAlignment(Qt.AlignmentFlag.AlignBottom)

        buttons.setContentsMargins(50, 0, 50, 0)
        buttons.setSpacing(50)

        buttons.addWidget(explore_button)
        buttons.addWidget(cancel_button)

        copy = QLabel(
            "©2026 Edgar Ayuso Martínez. Released under the MIT license.", self
        )
        copy.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(logo)
        layout.addWidget(heading)
        layout.addWidget(subheading)
        layout.addLayout(buttons)

        layout.addWidget(copy, alignment=Qt.AlignmentFlag.AlignBottom)
