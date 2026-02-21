"""Main window module"""

# pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon

from src.ui.intro.intro import Intro
from src.ui.dashboard.dashboard import Dashboard


class Window(QMainWindow):
    """Main window of the application"""

    def __init__(self, controller):
        super().__init__()

        self.setWindowTitle("NumChat: Chat Analizer")
        self.setGeometry(300, 300, 500, 350)
        self.setWindowIcon(QIcon("assets/icon.ico"))

        intro = Intro(controller, self)

        self.setCentralWidget(intro)

        controller.window = self

    def start_dashboard(self):
        """Starts the dashboard"""

        dashboard = Dashboard()

        self.setGeometry(200, 200, 700, 500)

        self.setWindowTitle("NumChat: Dashboard")

        self.setCentralWidget(dashboard)
