import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))

# pylint: disable=wrong-import-position
from src.app.app import App
from src.ui.window import Window

from src.core.controller import Controller


def main():

    app = App()

    app.setStyleSheet(Path("src/style/style.qss").read_text(encoding="UTF-8"))

    controller = Controller()

    window = Window(controller)
    window.show()

    app.mainloop()


if __name__ == "__main__":
    main()
