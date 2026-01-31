import sys

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QHBoxLayout
from PyQt6.QtCore import Qt

from src.core.controller import Engine


class Intro(QWidget):

    def __init__(self, engine: Engine, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout(self)

        self.setLayout(layout)

        instruction = QLabel("Select a JSON file", self)

        explore_button = QPushButton("Explore", self)
        explore_button.clicked.connect(lambda: engine.start())

        cancel_button = QPushButton("Cancel", self)
        cancel_button.clicked.connect(sys.exit)

        buttons = QHBoxLayout()

        buttons.setContentsMargins(50, 50, 50, 50)
        buttons.setSpacing(50)

        buttons.addWidget(explore_button)
        buttons.addWidget(cancel_button)

        layout.addWidget(instruction, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(buttons)
