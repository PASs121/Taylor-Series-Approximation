
from PyQt6.QtWidgets import QApplication
from gui import App

import sys

# This file contains the entry point for the Taylor series program, creating and running the QApplication and main window.


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = App()
    window.show()

    sys.exit(app.exec())