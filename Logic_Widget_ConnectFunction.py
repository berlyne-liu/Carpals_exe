# -*- coding: utf-8 -*-

from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem, QCursor
from PyQt5.QtWidgets import QMessageBox, QTableView, QFileDialog, QHeaderView, QDialog, QMenu, QTableWidgetItem, \
    QComboBox
from PyQt5.QtCore import QStringListModel
import os
import sqlite3
from xlwt import Workbook
from GUI_Carpals_Alarm import *
from GUI_Alarm_Config import *
from GUI_Dialog import Ui_DialogFrame
from Logic_Alarm_FileExtration import *
from Logic_Sqlite_Modify import *


class Widget_ConnectFunction(Ui_alarm, Ui_AlarmConfig, Ui_DialogFrame):
    def __init__(self):
        Ui_alarm.__init__(self)
        Ui_AlarmConfig.__init__(self)
        Ui_DialogFrame.__init__(self)
        self.slm = QStringListModel()
        self.alarm_setupUi()
        self.AlarmConfig_setupUi()
        self.connect = sqlite3.connect('./Carpals.db')
        self.sm = Sqlite_Modify(self.connect)
        self.Ae = Alarm_Extraction()
        # self.Path4 = "./Script/check_01.sql"
        self.add_list = []
        self.dic_AlarmFile = {}

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

    def frame_init(self, p_int):
        if p_int == 0:
            self.frame_as1.setHidden(True)
            self.frame_a.setHidden(False)
            self.Ontime_Query()
        elif p_int == 1:
            self.frame_as1.setHidden(False)
            self.frame_a.setHidden(True)

    def openfile(self, widget, mode="Main"):
        """
        openfile 是tool button点击后的实例方法
        功能：点击tool button后打开文件目录
        参数：n,用于将tool button与line Eidt对应起来
        """
        if mode == "Main":
            openfile_name = QFileDialog.getOpenFileName(self.centralwidget, '选择文件', '')
            file_name = openfile_name[0].split("/")[-1]
            widget.setText(openfile_name[0])
        elif mode == "Dialog":
            openfile_name = QFileDialog.getOpenFileName(self.child, '选择文件', '')
            file_name = openfile_name[0].split("/")[-1]
            widget.setText(openfile_name[0])

    def InitListview(self):
        _List = []
        self.slm.setStringList(_List)
        self.listView_a1.setModel(self.slm)

    def FuncListviewadditem(self, dictItem):
        _dicItem = dictItem
        if _dicItem:
            self.add_list = []
            for key, val in _dicItem.items():
                _strList = "将文件：" + str(key.split("/")[-1]) + "导入数据库：" + str(val)
                self.add_list.append(_strList)
                self.slm.setStringList(self.add_list)
                self.listView_a1.setModel(self.slm)
        else:
            self.InitListview()

    def ConnectListviewaddItem(self):
        add_path = self.lineEdit_a1.text()
        add_table = self.comboBox_a1.currentText()
        add_type = os.path.splitext(add_path)[-1]
        if len(add_path) * len(add_table) != 0:
            if add_type.lower() in (".csv", ".xlsx") or add_type.find(".") == -1:
                self.dic_AlarmFile[add_path] = add_table
                self.FuncListviewadditem(self.dic_AlarmFile)
            else:
                self.QMessageBoxShow("文件错误提示框", "您输入的文件路径不符合规则，请输入.txt/.xlsx/无扩展名的文件", 1)
                return
        else:
            self.QMessageBoxShow("错误提示框", "文件路径和导入数据表不能为空！", 1)
            return

    def listview_init(self):
        self.slm.setStringList([])
        self.listView_a1.setModel(self.slm)

    def listWidgetContext(self, point):
        popMenu = QMenu()
        pos = self.listView_a1.indexAt(point).column()  # 返回鼠标点击的位置的数据行，-1表示空白行
        if pos > -1:
            popMenu.addAction("修改", lambda: self.Dialog_exec(0))
            popMenu.addAction("删除", lambda: self.listview_delete(point))
            # print(QCursor.pos())
            popMenu.exec_(QCursor.pos())
        else:
            self.listView_a1.clearSelection()

    def QMessageBoxShow(self, title, message, p_int):
        if p_int == 0:  # mode 0:Question Type, No return value, Just Confirm whether the user operates correctly.
            QMessageBox.question(self, title, message, QMessageBox.Yes)
        elif p_int == 1:  # mode 1:Infomation Type, No return value, Just print the any string.
            QMessageBox.information(self, title, message, QMessageBox.Yes)
        elif p_int == 2:  # mode 2: Warning Type, return value, warning that the operate may be dangerous
            _choose = QMessageBox.warning(self, title, message, QMessageBox.Yes | QMessageBox.No)
            return _choose

    def Alarm_Generated(self):
        # Ae = Alarm_Extraction()
        for (path, table) in self.dic_AlarmFile.items():
            filetype = os.path.splitext(path)[-1]
            if filetype.lower() == ".csv":
                hea, cont, err = self.Ae.csvExtraction(path)
            elif filetype.lower() == ".xlsx":
                hea, cont, err = self.Ae.excelExtraction(path, mode="data", _sheetName="标准告警码")
            elif filetype.find(".") == -1:
                hea, cont, err = self.Ae.textExtraction(path)
            else:
                self.QMessageBoxShow("文件错误提示框", "您输入的文件路径不符合规则，请输入.txt/.xlsx/无扩展名的文件", 1)
                return
            self.sm.sqlite_insert(hea, cont, table=table)
        self.Ontime_Query()
        Alarm_result = self.sm.sqlite_query(path="./Script/Alarm_sql.sql")
        self.table_view(self.tableView_a1, Alarm_result)
        self.dic_AlarmFile.clear()

    def Ontime_Query(self):
        str_query = "select  'Alarm_Cause(告警信息)' as '数据表',count(*) as '实时数据量'," \
                    "datetime('now','localtime') as '查询时间' from Alarm_Cause union " \
                    "select  'Alarm_State(小区状态)' as '数据表',count(*) as '实时数据量'," \
                    "datetime('now','localtime') as '查询时间' from Alarm_State"
        Query_result = self.sm.sqlite_query(operation="query", query_Str=str_query)
        self.table_view(self.tableView_a2, Query_result)

    def Alarm_removedata(self):
        self.dic_AlarmFile.clear()
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

    def Dialog_exec(self, p_int):
        self.child = QDialog()
        child_ui = Ui_DialogFrame()
        if p_int == 0:
            child_ui.DialogAlarmUpdate_setupUi(self.child)
        elif p_int == 1:
            child_ui.DialogAlarmConfig_setupUi(self.child)
            self.DialogTableWidgetAddItems(child_ui)
            child_ui.toolButton_config1.released.connect(
                lambda: self.DialogAlarmConfigClickedFunc(child_ui.lineEdit_config1, child_ui))
            # child_ui.combobox_config1.currentIndexChanged.connect(lambda: self.DialogTableWidgetAddCombobox(child_ui))
            child_ui.combobox_config1.currentIndexChanged.connect(
                lambda: self.DialogOpenFileMatchTableWidgetItem(child_ui))
            child_ui.tablewidget_config1.clicked.connect(lambda: self.DialogTableWidgetAddCombobox(child_ui))
            child_ui.pushbutton_config1.released.connect(lambda: self.DialogConfigInsertButton(child_ui))
        self.child.show()

    def listview_delete(self):
        _Currenrow = self.listView_a1.currentIndex().row()
        for r, k in enumerate(list(self.dic_AlarmFile)):
            if r == _Currenrow:
                _value = self.QMessageBoxShow("信息删除告警!!", "是否取消将路径%s导入%s" % (k, self.dic_AlarmFile[k]), 2)
                if _value == 16384:
                    del self.dic_AlarmFile[k]
                    # print(self.dic_add)
                else:
                    break
        self.FuncListviewadditem(self.dic_AlarmFile)

    def DialogAlarmConfigClickedFunc(self, A_widget, dl):
        self.openfile(A_widget, mode="Dialog")
        _FilePath = A_widget.text()
        if _FilePath != "":
            _SheetName = self.Ae.excelExtraction(_FilePath, mode="sheet")
            dl.combobox_config1.addItems(_SheetName)
        else:
            return

    def DialogTableWidgetAddItems(self, dl):
        _id = self.buttonGroup_as1.checkedId()
        # comBox = QtWidgets.QComboBox()
        # comBox.setStyleSheet('QComboBox{margin:3px}')
        dicAlaConfig = {1: ["告警标题", "告警解析", "备注1", "备注2", "备注3"],
                        2: ["小区", "覆盖场景"],
                        3: ["ERBS", "ERBS中文名", "区域", "CELL", "小区中文名", "ABC网格", "综合网格35", "责任田125"],
                        4: []}
        for k, v in dicAlaConfig.items():
            if k == _id:
                for row, value in enumerate(v):
                    _len = len(v)
                    dl.tablewidget_config1.setRowCount(_len)
                    dl.tablewidget_config1.setItem(row, 0, QTableWidgetItem(value))

    def DialogTableWidgetAddCombobox(self, dl):
        _path = dl.lineEdit_config1.text()
        if _path != "":
            _currentSheet = dl.combobox_config1.currentText()
            _head = self.Ae.excelExtraction(_path, mode="header", _sheetName=_currentSheet)
            _rowCount = dl.tablewidget_config1.rowCount()
            _selectRow = dl.tablewidget_config1.selectionModel().selection().indexes()
            for n in range(_rowCount):
                dl.tablewidget_config1.removeCellWidget(n, 1)
            for i in _selectRow:
                if i.column() == 1:
                    comBox = QComboBox(dl.tablewidget_config1)
                    comBox.setObjectName(u'combobox_' + str(i.row()))
                    dl.tablewidget_config1.findChild(QComboBox, u'combobox_' + str(i.row())). \
                        setStyleSheet('QComboBox{''margin:3px}')
                    dl.tablewidget_config1.setCellWidget(i.row(), i.column(), dl.tablewidget_config1.
                                                         findChild(QComboBox, u'combobox_' + str(i.row())))
                    dl.tablewidget_config1.findChild(QComboBox, u'combobox_' + str(i.row())).clear()
                    dl.tablewidget_config1.findChild(QComboBox, u'combobox_' + str(i.row())).addItems(_head)
                    dl.tablewidget_config1.findChild(QComboBox, u'combobox_' + str(i.row())).\
                        setCurrentText(dl.tablewidget_config1.item(i.row(), i.column()).text())
                    dl.tablewidget_config1.findChild(QComboBox,
                                                     u'combobox_' + str(i.row())).currentIndexChanged.connect(
                        lambda: dl.tablewidget_config1.setItem(i.row(), i.column(),
                                                               QTableWidgetItem(dl.tablewidget_config1.
                                                                                findChild(QComboBox, u'combobox_' +
                                                                                          str(i.row())).currentText())))
        else:
            self.QMessageBoxShow("错误", "没有选择正确的文件路径，请选择！", p_int=0)

    def DialogOpenFileMatchTableWidgetItem(self, dl):
        _path = dl.lineEdit_config1.text()
        if _path != "":
            _currentSheet = dl.combobox_config1.currentText()
            _head = self.Ae.excelExtraction(_path, mode="header", _sheetName=_currentSheet)
            _rowcount = dl.tablewidget_config1.rowCount()
            for row1 in range(_rowcount):
                for row2 in range(len(_head)):
                    if _head[row2] == dl.tablewidget_config1.item(row1, 0).text():
                        dl.tablewidget_config1.setItem(row1, 1, QTableWidgetItem(_head[row2]))
                    else:
                        dl.tablewidget_config1.setItem(row1, 1, QTableWidgetItem(""))
        else:
            self.QMessageBoxShow("错误", "没有选择正确的文件路径，请选择！", p_int=0)

    def DialogConfigInsertButton(self, dl):
        _path = dl.lineEdit_config1.text()
        _rowCount = dl.tablewidget_config1.rowCount()
        _head: list = []
        if _path != "":
            for n in range(_rowCount):
                _head.append(dl.tablewidget_config1.item(n, 1).text())
            print(_head)
        else:
            self.QMessageBoxShow("错误", "没有选择正确的文件路径，请选择！", p_int=0)
