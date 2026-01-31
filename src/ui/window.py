# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QMainWindow
from src.ui.intro import Intro

from src.core.controller import Engine


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        engine = Engine()

        self.setGeometry(300, 300, 500, 350)
        self.setMaximumSize(500, 350)

        intro = Intro(engine, self)
        self.setCentralWidget(intro)

        self.setWindowTitle("Chat Analizer")
