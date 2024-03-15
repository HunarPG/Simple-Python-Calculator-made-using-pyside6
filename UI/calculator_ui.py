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
        Dialog.resize(662, 247)
        self.formLayout = QFormLayout(Dialog)
        self.formLayout.setObjectName(u"formLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_number_1 = QLineEdit(self.groupBox)
        self.le_number_1.setObjectName(u"le_number_1")

        self.gridLayout.addWidget(self.le_number_1, 0, 2, 1, 1)

        self.lb_result = QLabel(self.groupBox)
        self.lb_result.setObjectName(u"lb_result")

        self.gridLayout.addWidget(self.lb_result, 2, 0, 1, 1)

        self.lb_number_2 = QLabel(self.groupBox)
        self.lb_number_2.setObjectName(u"lb_number_2")

        self.gridLayout.addWidget(self.lb_number_2, 1, 0, 1, 1)

        self.lb_number_1 = QLabel(self.groupBox)
        self.lb_number_1.setObjectName(u"lb_number_1")

        self.gridLayout.addWidget(self.lb_number_1, 0, 0, 1, 1)

        self.le_number_2 = QLineEdit(self.groupBox)
        self.le_number_2.setObjectName(u"le_number_2")

        self.gridLayout.addWidget(self.le_number_2, 1, 2, 1, 1)

        self.l2_result = QLineEdit(self.groupBox)
        self.l2_result.setObjectName(u"l2_result")
        self.l2_result.setReadOnly(True)

        self.gridLayout.addWidget(self.l2_result, 2, 2, 1, 1)


        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.groupBox)

        self.pb_divide = QPushButton(Dialog)
        self.pb_divide.setObjectName(u"pb_divide")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_divide.sizePolicy().hasHeightForWidth())
        self.pb_divide.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.pb_divide)

        self.pb_multiply = QPushButton(Dialog)
        self.pb_multiply.setObjectName(u"pb_multiply")
        sizePolicy.setHeightForWidth(self.pb_multiply.sizePolicy().hasHeightForWidth())
        self.pb_multiply.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.pb_multiply)

        self.pb_subtract = QPushButton(Dialog)
        self.pb_subtract.setObjectName(u"pb_subtract")
        sizePolicy.setHeightForWidth(self.pb_subtract.sizePolicy().hasHeightForWidth())
        self.pb_subtract.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.pb_subtract)

        self.pb_add = QPushButton(Dialog)
        self.pb_add.setObjectName(u"pb_add")
        sizePolicy.setHeightForWidth(self.pb_add.sizePolicy().hasHeightForWidth())
        self.pb_add.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.pb_add)

        QWidget.setTabOrder(self.le_number_1, self.le_number_2)
        QWidget.setTabOrder(self.le_number_2, self.pb_add)
        QWidget.setTabOrder(self.pb_add, self.pb_subtract)
        QWidget.setTabOrder(self.pb_subtract, self.pb_multiply)
        QWidget.setTabOrder(self.pb_multiply, self.pb_divide)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Simple Calculator", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Type the numbers", None))
        self.lb_result.setText(QCoreApplication.translate("Dialog", u"Result is", None))
        self.lb_number_2.setText(QCoreApplication.translate("Dialog", u"Number 2", None))
        self.lb_number_1.setText(QCoreApplication.translate("Dialog", u"Number 1", None))
        self.pb_divide.setText(QCoreApplication.translate("Dialog", u"Divide", None))
        self.pb_multiply.setText(QCoreApplication.translate("Dialog", u"Multiply", None))
        self.pb_subtract.setText(QCoreApplication.translate("Dialog", u"Subtract", None))
        self.pb_add.setText(QCoreApplication.translate("Dialog", u"Add", None))
    # retranslateUi

