# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'GUI_Carpals.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QStyleFactory


class Ui_MainWindow(object):
    def __init__(self):
        self.icon = QtGui.QIcon()
        self.icon_1 = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("./icon/File.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_1.addPixmap(QtGui.QPixmap("./icon/title.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        # palette = QtGui.QPalette()
        # MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu2_1 = QtWidgets.QMenu(self.menu_2)
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.progressbar_1 = QtWidgets.QProgressBar(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setMenuBar(self.menubar)
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.action = QtWidgets.QAction(MainWindow)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_6 = QtWidgets.QAction(MainWindow)

        MainWindow.resize(1000, 600)
        # self.statusbar.setGeometry(QtCore.QRect(0, 550, 1000, 600))
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 70))
        self.menu.setGeometry(QtCore.QRect(256, 129, 120, 70))
        self.progressbar_1.setGeometry(0, 0, 100, 10)

        MainWindow.setAcceptDrops(True)
        MainWindow.setAnimated(True)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        self.menubar.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.statusbar.addPermanentWidget(self.progressbar_1)
        self.progressbar_1.setHidden(True)

        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.menu2_1.menuAction())
        self.menu2_1.addAction(self.action_3)
        self.menu2_1.addAction(self.action_4)
        self.menu_3.addAction(self.action_5)
        self.menu_3.addAction(self.action_6)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.menubar.setEnabled(True)
        self.menubar.setTabletTracking(False)
        self.menubar.setDefaultUp(False)
        # MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "网优日常小工具-专用版"))
        MainWindow.setWindowIcon(self.icon_1)
        self.menu.setTitle(_translate("MainWindow", "数据空间"))
        self.action.setText(_translate("MainWindow", "初始化"))
        self.action_2.setText(_translate("MainWindow", "清理数据库"))
        self.menu_2.setTitle(_translate("MainWindow", "指标体系"))
        self.menu2_1.setTitle(_translate("MainWindow", "导入数据"))
        self.action_3.setText(_translate("MainWindow", "固定格式导入"))
        self.action_4.setText(_translate("MainWindow", "自定义格式导入"))
        self.menu_3.setTitle(_translate("MainWindow", "告警处理"))
        self.action_5.setText(_translate("MainWindow", "LTE告警解析"))
        self.action_6.setText(_translate("MainWindow", "告警配置"))

    # def Dialog_setupUi(self, QDialog):
    #     self.Dialog = QtWidgets.QWidget(QDialog)
    #     QDialog.resize(400, 300)
    #     QDialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowCloseButtonHint)  # 设置窗体总显示在最上面
    #     QtCore.QMetaObject.connectSlotsByName(QDialog)
        # _translate = QtCore.QCoreApplication.translate
        # QDialog.setWindowTitle(_translate("QDialog", "QDialog"))
        # QDialog.setWindowIcon(self.icon_1)




