# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Carpals.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtCore import QPoint
from Logic_Widget_ConnectFunction import *


class Ui_signalContrl(Widget_ConnectFunction):
    def __init__(self):
        Widget_ConnectFunction.__init__(self)

    def QtWidget_Function(self):
        self.action_5.triggered.connect(lambda: self.frame_init(0))
        self.action_6.triggered.connect(lambda: self.frame_init(1))
        # toolbutton点击后（鼠标点击释放），打开文件目录
        self.toolButton_a1.released.connect(lambda: self.openfile(self.lineEdit_a1, mode="Main"))
        # Combobox 初始化：加入数据库的中的表名
        self.combobox_init(self.comboBox_a1, reg_name="Alarm")
        self.listView_a1.customContextMenuRequested[QPoint].connect(self.listWidgetContext)
        self.pushButton_a1.released.connect(self.Alarm_Export)
        self.pushButton_a2.released.connect(self.Alarm_Generated)
        self.pushButton_a3.released.connect(self.ConnectListviewaddItem)
        self.pushButton_a4.released.connect(self.Alarm_removedata)
        self.pushbutton_as1.released.connect(lambda: self.Dialog_exec(1))
        self.pushbutton_as2.released.connect(lambda: print(self.buttonGroup_as1.checkedId()))

