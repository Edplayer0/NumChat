import os
import sys
from pathlib import Path

path = Path(os.path.dirname(__file__)) / ".."

sys.path.insert(0, str(path))

# pylint: disable=wrong-import-position
from src.app.app import App
from src.ui.window import Window

from src.core.controller import Controller


def main():

    app = App()

    style = path / "src" / "style" / "style.qss"

    app.setStyleSheet(style.read_text(encoding="UTF-8"))

    controller = Controller()

    window = Window(controller)
    window.show()

    app.mainloop()


if __name__ == "__main__":
    main()
