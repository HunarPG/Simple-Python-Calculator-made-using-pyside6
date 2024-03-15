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
        self.l2_result.setText(f"{float(self.le_number_1.text()) + float(self.le_number_2.text())}")
    @qtc.Slot()
    def subtract(self):
        self.l2_result.setText(f"{float(self.le_number_1.text()) - float(self.le_number_2.text())}")
    @qtc.Slot()
    def multiply(self):
        self.l2_result.setText(f"{float(self.le_number_1.text()) * float(self.le_number_2.text())}")
    @qtc.Slot()
    def divide(self):
        self.l2_result.setText(f"{float(self.le_number_1.text()) / float(self.le_number_2.text())}")

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
