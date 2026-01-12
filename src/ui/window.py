# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QWidget, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args):
        super().__init__()

        self.setGeometry(200, 200, 800, 550)

        self.setWindowTitle("Telegram Chat Analizer")

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        main_layout.setContentsMargins(50, 100, 50, 100)

        for component in args:
            main_layout.addLayout(component)
