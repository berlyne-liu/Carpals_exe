# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Carpals.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QMainWindow, QDialog, QFileDialog
from GUI_Carpals_test import *


class Ui_DialogFrame(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        # self.Dialog_setupUi(self)

    def DialogAlarmUpdate_setupUi(self, Dialog):
        self.frame_dl1 = QtWidgets.QFrame(Dialog)
        self.pushButton_dl1 = QtWidgets.QPushButton(self.frame_dl1)
        self.frame_dl1.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.pushButton_dl1.setGeometry(QtCore.QRect(160, 100, 75, 23))
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowCloseButtonHint)  # 设置窗体总显示在最上面
        QtCore.QMetaObject.connectSlotsByName(self.frame_dl1)
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "更新"))
        Dialog.setWindowIcon(self.icon_1)
        self.pushButton_dl1.setText(_translate("Dialog", "PushButton"))

    def DialogAlarmConfig_setupUi(self, Dialog):
        Dialog.resize(600, 400)
        self.frame_config = QtWidgets.QFrame(Dialog)
        self.lable_config1 = QtWidgets.QLabel(self.frame_config)
        self.lable_config2 = QtWidgets.QLabel(self.frame_config)
        self.lineEdit_config1 = QtWidgets.QLineEdit(self.frame_config)
        self.toolButton_config1 = QtWidgets.QToolButton(self.frame_config)
        self.combobox_config1= QtWidgets.QComboBox(self.frame_config)
        self.tablewidget_config1 = QtWidgets.QTableWidget(self.frame_config)
        self.pushbutton_config1 = QtWidgets.QPushButton(self.frame_config)

        self.frame_config.setGeometry(QtCore.QRect(0, 0, 600, 400))
        self.lable_config1.setGeometry(QtCore.QRect(10, 10, 100, 30))
        self.lable_config2.setGeometry(QtCore.QRect(10, 50, 100, 30))
        self.lineEdit_config1.setGeometry(QtCore.QRect(120, 10, 400, 30))
        self.toolButton_config1.setGeometry(QtCore.QRect(520, 10, 30, 30))
        self.combobox_config1.setGeometry(QtCore.QRect(120, 50, 150, 30))
        self.tablewidget_config1.setGeometry(QtCore.QRect(10, 90, 580, 230))
        self.pushbutton_config1.setGeometry(QtCore.QRect(500, 340, 90, 40))

        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowCloseButtonHint)  # 设置窗体总显示在最上面
        QtCore.QMetaObject.connectSlotsByName(self.frame_config)
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "导入数据"))
        Dialog.setWindowIcon(self.icon_1)
        self.lable_config1.setText(_translate("Dialog", "请选择文件："))
        self.lable_config2.setText(_translate("Dialog", "请选择工作表："))
        self.pushbutton_config1.setText(_translate("Dialog", "导入"))
        self.toolButton_config1.setText(_translate("Dialog", "文件"))
        self.toolButton_config1.setIcon(self.icon)

        self.toolButton_config1.released.connect(lambda: self.Dialogopenfile(self.lineEdit_config1))

    def Dialogopenfile(self, widget):
        """
        openfile 是tool button点击后的实例方法
        功能：点击tool button后打开文件目录
        参数：n,用于将tool button与line Eidt对应起来
        """
        openfile_name = QFileDialog.getOpenFileName(Dialog, '选择文件', '')
        file_name = openfile_name[0].split("/")[-1]
        widget.setText(openfile_name[0])
