import sys
import pathlib

from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox,
    QLabel, QComboBox, QLineEdit, QSlider, QPushButton, QSpinBox
)
from PyQt6.QtGui import QIcon
from PyQt6 import uic

from plotter import Plotter
from lib import sine, cosine, exponential
from math import sin, cos, exp

ui_path = str(pathlib.Path("ui/gui.ui").absolute())
close_icon_path = str(pathlib.Path("assets/x-circle.png").absolute())
window_icon_path = str(pathlib.Path("assets/window-icon.png").absolute())
graph_icon_path = str(pathlib.Path("assets/graph-icon.svg").absolute())
calc_icon_path = str(pathlib.Path("assets/calculate-icon.svg").absolute())

class App(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        try:
            self.ui = uic.loadUi(ui_path, self)

        except Exception as e:
            print(f"Error loading UI: {e}")
            print("\nEdit the path to the .ui file in gui.py.")

            QMessageBox.critical(
                self, 
                "Error", 
                f"Error loading UI: {e}\n\nEdit the path to the .ui file in gui.py."
                )
            
            sys.exit(1)

        self.setWindowIcon(QIcon(window_icon_path))

        self.plotter = Plotter()
        self.functions = {"sine": [sine, sin], "cosine": [cosine, cos], "exp": [exponential, exp]}

        self.closeButton : QPushButton = self.findChild(QPushButton, "closeButton")

        self.functionSelect : QComboBox = self.findChild(QComboBox, "functionSelect")
        self.functionSelect_2 : QComboBox = self.findChild(QComboBox, "functionSelect_2")

        self.taylorLabel : QLabel = self.findChild(QLabel, "taylorLabel")
        self.actualLabel : QLabel = self.findChild(QLabel, "actualLabel")

        self.termSlider : QSlider = self.findChild(QSlider, "termSlider")
        self.termsBox : QSpinBox = self.findChild(QSpinBox, "termsBox")

        self.termSlider_2 : QSlider = self.findChild(QSlider, "termSlider_2")
        self.termsBox_2 : QSpinBox = self.findChild(QSpinBox, "termsBox_2")

        self.rangeSlider : QSlider = self.findChild(QSlider, "rangeSlider")
        self.rangeBox : QSpinBox = self.findChild(QSpinBox, "rangeBox")

        self.xValue : QLineEdit = self.findChild(QLineEdit, "xValue")

        self.taylorValue : QLabel = self.findChild(QLabel, "taylorValue")
        self.actualValue : QLabel = self.findChild(QLabel, "actualValue")

        self.calcButton : QPushButton = self.findChild(QPushButton, "calcButton")
        self.graphButton : QPushButton = self.findChild(QPushButton, "graphButton")

        self.init_ui()

        self.calcButton.clicked.connect(self.calculate)
        self.graphButton.clicked.connect(self.plot)

        self.termSlider.valueChanged.connect(self.update_terms)
        self.termsBox.valueChanged.connect(self.update_terms)

        self.termSlider_2.valueChanged.connect(self.update_terms)
        self.termsBox_2.valueChanged.connect(self.update_terms)

        self.rangeSlider.valueChanged.connect(self.update_terms)
        self.rangeBox.valueChanged.connect(self.update_terms)

        self.functionSelect.currentIndexChanged.connect(self.update_labels)

        self.closeButton.clicked.connect(self.close)

    def calculate(self) -> None:

        try:
            x = float(self.xValue.text())
            terms = self.termSlider.value()
            function = self.functionSelect.currentText()

            taylor_func, actual_func = self.functions[function]

            taylor_result = taylor_func(x, terms)
            actual_result = actual_func(x)

            self.taylorValue.setText(f"{taylor_result:.5f}")
            self.actualValue.setText(f"{actual_result:.5f}")

        except ValueError:
            QMessageBox.warning(
                self, 
                "Invalid Input", 
                "Please enter a valid number for x."
                )
            
    def plot(self) -> None:

        function = self.functionSelect_2.currentText()
        terms = self.termSlider_2.value()
        plot_range = self.rangeSlider.value()

        plot_functions = {'sine': self.plotter.plot_sine, 'cosine': self.plotter.plot_cosine, 'exp': self.plotter.plot_exponential}

        plot_func = plot_functions[function]
        plot_func(terms, plot_range)

    def update_labels(self) -> None:
        function = self.functionSelect.currentText()

        if function == "sine":
            self.taylorLabel.setText("Taylor series sin(x):")
            self.actualLabel.setText("Actual sin(x):")

        elif function == "cosine":
            self.taylorLabel.setText("Taylor series cos(x):")
            self.actualLabel.setText("Actual cos(x):")

        elif function == "exp":
            self.taylorLabel.setText("Taylor series exp(x):")
            self.actualLabel.setText("Actual exp(x):")

        else:
            pass

    def update_terms(self) -> None:
        
        sender = self.sender()

        if sender == self.termSlider:
            terms = self.termSlider.value()
            self.termsBox.setValue(terms)

        elif sender == self.termsBox:
            terms = self.termsBox.value()
            self.termSlider.setValue(terms)

        elif sender == self.termSlider_2:
            terms = self.termSlider_2.value()
            self.termsBox_2.setValue(terms)

        elif sender == self.termsBox_2:
            terms = self.termsBox_2.value()

            self.termSlider_2.setValue(terms)
        elif sender == self.rangeSlider:
            plot_range = self.rangeSlider.value()
            self.rangeBox.setValue(plot_range)

        elif sender == self.rangeBox:
            plot_range = self.rangeBox.value()
            self.rangeSlider.setValue(plot_range)

        else:
            pass

    def init_ui(self) -> None:

        self.taylorValue.setText("  -  ")
        self.actualValue.setText("  -  ")

        self.closeButton.setIcon(QIcon(close_icon_path))
        self.calcButton.setIcon(QIcon(calc_icon_path))
        self.graphButton.setIcon(QIcon(graph_icon_path))

        self.termSlider.setMinimum(1)
        self.termSlider.setMaximum(100)
        self.termSlider.setValue(50)

        self.termSlider_2.setMinimum(1)
        self.termSlider_2.setMaximum(100)
        self.termSlider_2.setValue(50)

        self.rangeSlider.setMinimum(1)
        self.rangeSlider.setMaximum(20)
        self.rangeSlider.setValue(4)

        self.termsBox.setMinimum(1)
        self.termsBox.setMaximum(100)
        self.termsBox.setValue(50)

        self.termsBox_2.setMinimum(1)
        self.termsBox_2.setMaximum(100)
        self.termsBox_2.setValue(50)

        self.rangeBox.setMinimum(1)
        self.rangeBox.setMaximum(20)
        self.rangeBox.setValue(4)

    def reset_all(self) -> None:
        
        self.functionSelect.setCurrentIndex(0)
        self.functionSelect_2.setCurrentIndex(0)

        self.taylorValue.setText("  -  ")
        self.actualValue.setText("  -  ")

        self.termSlider.setValue(50)
        self.termSlider_2.setValue(50)
        self.rangeSlider.setValue(4)

        self.termsBox.setValue(50)
        self.termsBox_2.setValue(50)
        self.rangeBox.setValue(4)

        self.xValue.clear()

    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key.Key_R and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            
            button = QMessageBox.question(
                self,
                "Reset Confirmation",
                "Are you sure you want to reset all fields?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            
            if button == QMessageBox.StandardButton.Yes:
                self.reset_all()

if __name__ == "__main__":
    print("This is module for the GUI of the sin_cos program. \nRun main.py to start the application.")