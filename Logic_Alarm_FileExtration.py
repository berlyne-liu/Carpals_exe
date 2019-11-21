# -*- coding: utf-8 -*-

import csv
import xlrd


class Alarm_Extraction:
    def textExtraction(self, filepath):
        container = []
        error = "存在以下异常：\n"
        try:
            with open(filepath, 'r') as file:
                file_list = file.readlines()
                t_header = file_list[3].strip('\n').split('\t')
                column_h = len(t_header)
                for row in range(len(file_list)):
                    package = file_list[row].strip('\n').split('\t')
                    if row > 0 and len(package) == column_h:
                        container.append(package)
                    else:
                        error = error + ("第%s行的字段数为%s,不符合规则！\n" % (row, len(package)))
        except Exception as e:
            error = error + str(e)
            t_header = None
        return t_header, container, error

    def csvExtraction(self, csvpath):
        container = []
        error = "存在以下异常：\n"
        try:
            with open(csvpath, 'r') as file:
                cr = csv.reader(file, delimiter="|", quotechar='"')
                for i, rows in enumerate(cr):
                    if i > 0:
                        container.append(rows)
                c_header = container[0]
        except Exception as e:
            error = error + str(e)
            c_header = None
        return c_header, container, error

    def excelExtraction(self, excelpath, mode="data", _sheetName=None):
        container = []
        error = "存在以下异常：\n"
        excelFile = xlrd.open_workbook(excelpath)
        if mode == "data":
            try:
                table = excelFile.sheet_by_name(_sheetName)
                r = table.nrows
                e_header = table.row_values(rowx=0, start_colx=0, end_colx=None)
                for i in range(r):
                    if i > 0:
                        container.append(table.row_values(rowx=i, start_colx=0, end_colx=None))
            except Exception as e:
                error = error + str(e)
                e_header = None
            return e_header, container, error
        elif mode == "sheet":
            sheet_name = excelFile.sheet_names()
            return sheet_name
        elif mode == "header":
            table = excelFile.sheet_by_name(_sheetName)
            e_header = table.row_values(rowx=0, start_colx=0, end_colx=None)
            return e_header

    def testfunc(self, path, Colindex, _sheetName=None):
        excelFile = xlrd.open_workbook(path)
        table = excelFile.sheet_by_name(_sheetName)
        _coly: list =[]
        for n, v in enumerate(Colindex):
            _coly.append(table.col_values(colx=v, start_rowx=0, end_rowx=3))
        for row in range(len(_coly)):
            if row == 0:
                row1 = _coly[row]
            else:
                pass

        print(_coly)


if __name__ == '__main__':
    path = "C:/Users/My-PC/Desktop/LTE告警汇总20191002.xlsx"
    sheetName = "Sheet4"
    _selectedColx = (1, 4, 6)
    # ae = Alarm_Extraction()
    # ae.testfunc(path, _selectedColx, _sheetName=sheetName)
    list1 = [1, 2, 3, 4]
    list2 = ["z", "x", "c", "v"]
    list3 = list(zip(list1, list2))
    print(list3)
