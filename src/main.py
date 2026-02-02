import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))

# pylint: disable=wrong-import-position
from src.app.app import App
from src.ui.window import MainWindow


def main():

    app = App()

    app.setStyleSheet(Path("src/styles/intro.qss").read_text(encoding="UTF-8"))

    window = MainWindow()
    window.show()

    app.mainloop()


if __name__ == "__main__":
    main()
