
from PyQt6.QtWidgets import QApplication
from gui import App

import sys


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = App()
    window.show()

    sys.exit(app.exec())