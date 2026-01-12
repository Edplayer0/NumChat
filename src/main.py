import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

# pylint: disable=wrong-import-position
from src.app.app import App
from src.ui.window import MainWindow

# GUI Components
from src.ui.intro import Intro


def main():

    app = App()

    root = MainWindow(Intro().layout)
    root.show()

    app.mainloop()


if __name__ == "__main__":
    main()
