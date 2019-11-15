# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Carpals.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QMainWindow
from GUI_Carpals_test import *


class Ui_DialogFrame(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def DialogAlarmUpdate_setupUi(self, Dialog):
        self.frame_dl1 = QtWidgets.QFrame(Dialog)
        self.pushButton_dl1 = QtWidgets.QPushButton(self.frame_dl1)
        self.frame_dl1.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.pushButton_dl1.setGeometry(QtCore.QRect(160, 100, 75, 23))
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowCloseButtonHint)  # 设置窗体总显示在最上面
        QtCore.QMetaObject.connectSlotsByName(self.frame_dl1)
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_dl1.setText(_translate("Dialog", "PushButton"))

    def DialogAlarmConfig_setupUi(self, Dialog):
        self.frame_config = QtWidgets.QFrame(Dialog)
        self.lable_config1 = QtWidgets.QLabel(self.frame_config)
        self.lable_config2 = QtWidgets.QLabel(self.frame_config)
        self.lineEdit_config1 = QtWidgets.QLineEdit(self.frame_config)
        self.combobox_config1= QtWidgets.QComboBox(self.frame_config)
        self.tablewidget_config1 = QtWidgets.QTableWidget(self.frame_config)
        self.pushbutton_config1 = QtWidgets.QPushButton(self.frame_config)

        self.frame_config.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.lable_config1.setGeometry(QtCore.QRect())
        self.lable_config2.setGeometry(QtCore.QRect())
        self.lineEdit_config1.setGeometry(QtCore.QRect())
        self.combobox_config1.setGeometry(QtCore.QRect())
        self.tablewidget_config1.setGeometry(QtCore.QRect())
        self.pushbutton_config1.setGeometry(QtCore.QRect())

        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowCloseButtonHint)  # 设置窗体总显示在最上面
        QtCore.QMetaObject.connectSlotsByName(self.frame_config)
        _translate = QtCore.QCoreApplication.translate


