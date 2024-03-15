import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from UI.calculator_ui import Ui_Dialog

class Calculator(qtw.QWidget, Ui_Dialog ):
    multiplied = qtc.Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_add.clicked.connect(self.add)
        self.pb_subtract.clicked.connect(self.subtract)
        self.pb_multiply.clicked.connect(self.multiply)
        self.pb_divide.clicked.connect(self.divide)
    @qtc.Slot()
    def add(self):
        self.lb_result.setText(f"Result is {float(self.le_first_number.text()) + float(self.le_second_number.text())}")
    @qtc.Slot()
    def subtract(self):
        self.lb_result.setText(f"Result is {float(self.le_first_number.text()) - float(self.le_second_number.text())}")
    @qtc.Slot()
    def multiply(self):
        self.lb_result.setText(f"Result is {float(self.le_first_number.text()) * float(self.le_second_number.text())}")
    @qtc.Slot()
    def divide(self):
        self.lb_result.setText(f"Result is {float(self.le_first_number.text()) / float(self.le_second_number.text())}")

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
