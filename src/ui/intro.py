# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QPushButton


class Intro:
    def __init__(self):

        layout = QVBoxLayout()

        instruction = QLabel("Select a JSON file")
        button = QPushButton("Explore")

        layout.addWidget(instruction)
        layout.addWidget(button)
