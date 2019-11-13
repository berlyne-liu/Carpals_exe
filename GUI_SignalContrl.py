# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Carpals.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import QStringListModel, QPoint
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox, QTableView, QFileDialog, QHeaderView, QDialog
import os
import sqlite3
from xlwt import Workbook
from GUI_Carpals_Alarm import *
from Logic_Alarm_FileExtration import *
from Logic_Sqlite_Modify import *


class Ui_signalContrl(Ui_alarm):
    def __init__(self):
        Ui_alarm.__init__(self)
        self.slm = QStringListModel()
        self.alarm_setupUi()
        self.connect = sqlite3.connect('./Carpals.db')
        self.sm = Sqlite_Modify(self.connect)
        self.file_path1 = None
        self.file_path2 = None
        self.file_path3 = None
        self.file_path4 = None
        self.file_path5 = None
        # self.Path4 = "./Script/check_01.sql"
        self.add_list = []
        self.dic_add = {}

    def QtWidget_Funtion(self):
        self.action_5.triggered.connect(lambda: self.frame_init())
        # toolbutton点击后（鼠标点击释放），打开文件目录
        self.toolButton_a1.released.connect(lambda: self.openfile(5))
        # Combobox 初始化：加入数据库的中的表名
        self.combobox_init(self.comboBox_a1, reg_name="Alarm")
        self.listView_a1.customContextMenuRequested[QPoint].connect(self.listWidgetContext)
        self.pushButton_a1.released.connect(lambda: self.Alarm_Export())
        self.pushButton_a2.released.connect(lambda: self.Alarm_Generated())
        self.pushButton_a3.released.connect(self.ConnectListviewaddItem)
        self.pushButton_a4.released.connect(lambda: self.Alarm_removedata())

    def combobox_init(self, widget, reg_name=None):
        container = []
        sq = self.sm.sqlite_query("./Script/check_01.sql")
        for num, rows in enumerate(sq):
            if rows[0][:rows[0].index("_")] == reg_name:
                container.append(rows[0])
        # print(container)
        if len(container):
            widget.clear()
            widget.addItems(container)
            widget.setCurrentIndex(-1)
        else:
            widget.clear()
            widget.addItem("数据库无相关表数据")
            # widget.setCurrentIndex(-1)

    def frame_init(self):
        self.frame_a.setHidden(False)
        self.Ontime_Query()

    def openfile(self, n):
        """
        openfile 是tool button点击后的实例方法
        功能：点击tool button后打开文件目录
        参数：n,用于将tool button与line Eidt对应起来
        """
        openfile_name = QFileDialog.getOpenFileName(self.centralwidget, '选择文件', '')
        file_name = openfile_name[0].split("/")[-1]
        # print('linetext_{0}被输入数据：'.format(n) + openfile_name[0])
        # print('文件名为：' + file_name)
        if n == 1:
            # print(self.lineEdit_1.text())
            self.lineEdit_1.setText(openfile_name[0])
            self.file_path1 = openfile_name[0]
            # print(self.file_path1)
        elif n == 2:
            self.lineEdit_2.setText(openfile_name[0])
            self.file_path2 = openfile_name[0]
        elif n == 3:
            self.lineEdit_3.setText(openfile_name[0])
            self.file_path3 = openfile_name[0]
        elif n == 4:
            self.lineEdit_4.setText(openfile_name[0])
            self.file_path4 = openfile_name[0]
        elif n == 5:
            self.lineEdit_a1.setText(openfile_name[0])
            self.file_path5 = openfile_name[0]

    def InitListview(self):
        self.slm.setStringList([])
        self.listView_a1.setModel(self.slm)

    def FuncListviewadditem(self, dictItem):
        _dicItem = dictItem
        for key, val in _dicItem.items():
            _strList = "将文件：" + str(key.split("/")[-1]) + "导入数据库：" + str(val)
            self.add_list.append(_strList)
            self.slm.setStringList(self.add_list)
            self.listView_a1.setModel(self.slm)

    def ConnectListviewaddItem(self):
        add_path = self.lineEdit_a1.text()
        add_table = self.comboBox_a1.currentText()
        add_type = os.path.splitext(add_path)[-1]
        if len(add_path) * len(add_table) != 0:
            if add_type.lower() in (".csv", ".xlsx") or add_type.find(".") == -1:
                self.dic_add[add_path] = add_table
                self.FuncListviewadditem(self.dic_add)
            else:
                self.QMessageBoxShow("文件错误提示框", "您输入的文件路径不符合规则，请输入.txt/.xlsx/无扩展名的文件")
                return
        else:
            self.QMessageBoxShow("错误提示框", "文件路径和导入数据表不能为空！")
            return

    def listview_init(self):
        self.slm.setStringList([])
        self.listView_a1.setModel(self.slm)

    def listWidgetContext(self, point):
        popMenu = QMenu()
        pos = self.listView_a1.indexAt(point).column()  # 返回鼠标点击的位置的数据行，-1表示空白行
        if pos > -1:
            popMenu.addAction("修改", lambda: self.Dialog_exec())
            popMenu.addAction("删除", lambda: self.listview_delete(point))
            # print(QCursor.pos())
            popMenu.exec_(QCursor.pos())
        else:
            self.listView_a1.clearSelection()

    def QMessageBoxShow(self, title, message):
        QMessageBox.warning(self, title, message, QMessageBox.Yes | QMessageBox.No)

    def Alarm_Generated(self):
        Ae = Alarm_Extraction()
        for (path, table) in self.dic_add.items():
            filetype = os.path.splitext(path)[-1]
            if filetype.lower() == ".csv":
                hea, cont, err = Ae.csvExtraction(path)
            elif filetype.lower() == ".xlsx":
                hea, cont, err = Ae.excelExtraction(path)
            elif filetype.find(".") == -1:
                hea, cont, err = Ae.textExtraction(path)
            else:
                self.QMessageBoxShow("文件错误提示框", "您输入的文件路径不符合规则，请输入.txt/.xlsx/无扩展名的文件")
                return
            self.sm.sqlite_insert(hea, cont, table=table)
        self.Ontime_Query()
        Alarm_result = self.sm.sqlite_query(path="./Script/Alarm_sql.sql")
        self.table_view(self.tableView_a1, Alarm_result)
        self.dic_add.clear()

    def Ontime_Query(self):
        str_query = "select  'Alarm_Cause(告警信息)' as '数据表',count(*) as '实时数据量'," \
                    "datetime('now','localtime') as '查询时间' from Alarm_Cause union " \
                    "select  'Alarm_State(小区状态)' as '数据表',count(*) as '实时数据量'," \
                    "datetime('now','localtime') as '查询时间' from Alarm_State"
        Query_result = self.sm.sqlite_query(operation="query", query_Str=str_query)
        self.table_view(self.tableView_a2, Query_result)

    def Alarm_removedata(self):
        self.dic_add.clear()
        self.sm.sqlite_query(operation="delete", configure="Alarm")
        self.Alarm_init()

    def table_view(self, widget, result):
        model = QStandardItemModel()
        model.clear()
        font_a1 = self.Tableview_setFont()
        desc = self.sm.cur.description
        h = [data[0] for data in desc]
        model.setHorizontalHeaderLabels(h)
        widget.setFont(font_a1)
        widget.setEditTriggers(QTableView.NoEditTriggers)
        # widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        widget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for row, data in enumerate(result):
            for column, item in enumerate(data):
                i = QStandardItem(str(item)) if item is not None else QStandardItem('')
                model.setItem(row, column, i)
        widget.setModel(model)

    def Tableview_setFont(self, family="Microsoft YaHei", size=7, bold=False, weight=10):
        font = QFont()
        font.setFamily(family)
        font.setPointSize(size)
        font.setBold(bold)
        font.setWeight(weight)
        return font

    def Alarm_init(self):
        self.add_list.clear()
        self.lineEdit_a1.clear()
        self.comboBox_a1.setCurrentIndex(-1)
        self.slm.setStringList(self.add_list)
        self.listView_a1.setModel(self.slm)
        self.tableView_a1.setModel(None)
        self.Ontime_Query()

    def Alarm_Export(self):
        Alarm_result = self.sm.sqlite_query("./Script/Alarm_sql.sql")
        h = [data[0] for data in self.sm.cur.description]
        book = Workbook()
        sheet = book.add_sheet("告警表")
        for rowx, head in enumerate(h):
            sheet.write(0, rowx, head)
        for rowy, row in enumerate(Alarm_result):
            for colx, text in enumerate(row):
                sheet.write(rowy + 1, colx, text)
        book.save("./Result/告警表.xls")

    def Dialog_exec(self):
        self.child = QDialog()
        child_ui = Ui_MainWindow()
        child_ui.Dialog_setupUi(self.child)
        self.child.show()

    def listview_delete(self, point):
        column = self.listView_a1.indexAt(point).column()
        self.QMessageBoxShow("警告", "将删除第%s行，删除后无法复原，请谨慎操作！！" % (column+1))
        #     add_path =
        # add_str = "将文件：" + str(add_path.split("/")[-1]) + "导入数据库：" + str(add_table)
        # self.add_list.append(add_str)
        # self.slm.setStringList(self.add_list)
        # self.listView_a1.setModel(self.slm)



