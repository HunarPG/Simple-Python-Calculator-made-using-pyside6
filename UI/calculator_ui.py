# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(774, 239)
        self.formLayout = QFormLayout(Dialog)
        self.formLayout.setObjectName(u"formLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_second_number = QLineEdit(self.groupBox)
        self.le_second_number.setObjectName(u"le_second_number")

        self.gridLayout.addWidget(self.le_second_number, 1, 1, 1, 1)

        self.le_first_number = QLineEdit(self.groupBox)
        self.le_first_number.setObjectName(u"le_first_number")

        self.gridLayout.addWidget(self.le_first_number, 0, 1, 1, 1)

        self.lb_second_number = QLabel(self.groupBox)
        self.lb_second_number.setObjectName(u"lb_second_number")

        self.gridLayout.addWidget(self.lb_second_number, 1, 0, 1, 1)

        self.lb_first_number = QLabel(self.groupBox)
        self.lb_first_number.setObjectName(u"lb_first_number")

        self.gridLayout.addWidget(self.lb_first_number, 0, 0, 1, 1)

        self.lb_result = QLabel(self.groupBox)
        self.lb_result.setObjectName(u"lb_result")

        self.gridLayout.addWidget(self.lb_result, 2, 0, 1, 1)


        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.groupBox)

        self.pb_add = QPushButton(Dialog)
        self.pb_add.setObjectName(u"pb_add")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_add.sizePolicy().hasHeightForWidth())
        self.pb_add.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.pb_add)

        self.pb_subtract = QPushButton(Dialog)
        self.pb_subtract.setObjectName(u"pb_subtract")
        sizePolicy.setHeightForWidth(self.pb_subtract.sizePolicy().hasHeightForWidth())
        self.pb_subtract.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.pb_subtract)

        self.pb_multiply = QPushButton(Dialog)
        self.pb_multiply.setObjectName(u"pb_multiply")
        sizePolicy.setHeightForWidth(self.pb_multiply.sizePolicy().hasHeightForWidth())
        self.pb_multiply.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.pb_multiply)

        self.pb_divide = QPushButton(Dialog)
        self.pb_divide.setObjectName(u"pb_divide")
        sizePolicy.setHeightForWidth(self.pb_divide.sizePolicy().hasHeightForWidth())
        self.pb_divide.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.pb_divide)

        QWidget.setTabOrder(self.le_first_number, self.le_second_number)
        QWidget.setTabOrder(self.le_second_number, self.pb_add)
        QWidget.setTabOrder(self.pb_add, self.pb_subtract)
        QWidget.setTabOrder(self.pb_subtract, self.pb_multiply)
        QWidget.setTabOrder(self.pb_multiply, self.pb_divide)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Simple Calculator", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Multiply two Numbers", None))
        self.lb_second_number.setText(QCoreApplication.translate("Dialog", u"Second Number", None))
        self.lb_first_number.setText(QCoreApplication.translate("Dialog", u"First  Number", None))
        self.lb_result.setText(QCoreApplication.translate("Dialog", u"Result", None))
        self.pb_add.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.pb_subtract.setText(QCoreApplication.translate("Dialog", u"Subtract", None))
        self.pb_multiply.setText(QCoreApplication.translate("Dialog", u"Multiply", None))
        self.pb_divide.setText(QCoreApplication.translate("Dialog", u"Divide", None))
    # retranslateUi

