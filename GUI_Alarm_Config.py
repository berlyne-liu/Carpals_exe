# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Carpals.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QMainWindow
from GUI_Carpals_test import *


class Ui_AlarmSetup(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def AlarmSetup_setupUi(self):
        self.frame_as1 = QtWidgets.QFrame(self.centralwidget)
        self.groupbox_as1 = QtWidgets.QGroupBox(self.frame_as1)
        self.pushbutton_as1 = QtWidgets.QPushButton(self.groupbox_as1)
        self.pushbutton_as2 = QtWidgets.QPushButton(self.groupbox_as1)
        self.pushbutton_as3 = QtWidgets.QPushButton(self.groupbox_as1)
        self.RadioButton_as1 = QtWidgets.QRadioButton(self.groupbox_as1)
        self.RadioButton_as2 = QtWidgets.QRadioButton(self.groupbox_as1)
        self.RadioButton_as3 = QtWidgets.QRadioButton(self.groupbox_as1)
        self.RadioButton_as4 = QtWidgets.QRadioButton(self.groupbox_as1)
        self.Tableview_as1 = QtWidgets.QTableView(self.frame_as1)

        self.frame_as1.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.groupbox_as1.setGeometry(QtCore.QRect(10, 5, 980, 100))
        self.pushbutton_as1.setGeometry(QtCore.QRect(230, 40, 90, 40))
        self.pushbutton_as2.setGeometry(QtCore.QRect(330, 40, 90, 40))
        self.pushbutton_as3.setGeometry(QtCore.QRect(430, 40, 90, 40))
        self.RadioButton_as1.setGeometry(QtCore.QRect(20, 30, 90, 20))
        self.RadioButton_as2.setGeometry(QtCore.QRect(130, 30, 90, 20))
        self.RadioButton_as3.setGeometry(QtCore.QRect(20, 70, 90, 20))
        self.RadioButton_as4.setGeometry(QtCore.QRect(130, 70, 90, 20))
        self.Tableview_as1.setGeometry(QtCore.QRect(10, 120, 980, 420))

        self.frame_as1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_as1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_as1.setEnabled(True)
        self.frame_as1.setHidden(True)
        self.frame_as1.setAutoFillBackground(False)
        self.frame_as1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_as1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RadioButton_as4.setEnabled(False)

        self.AlarmSetup_retranslateUi()

    def AlarmSetup_retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushbutton_as1.setText(_translate("MainWindow", "导入"))
        self.pushbutton_as2.setText(_translate("MainWindow", "呈现"))
        self.pushbutton_as3.setText(_translate("MainWindow", "导出"))
        self.RadioButton_as1.setText(_translate("MainWindow", "告警花名册"))
        self.RadioButton_as2.setText(_translate("MainWindow", "覆盖场景"))
        self.RadioButton_as3.setText(_translate("MainWindow", "LTE工参信息"))
        self.RadioButton_as4.setText(_translate("MainWindow", ""))
