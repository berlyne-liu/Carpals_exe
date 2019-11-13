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

    def excelExtraction(self, excelpath):
        container = []
        error = "存在以下异常：\n"
        try:
            excelFile = xlrd.open_workbook(excelpath)
            sheet_name = excelFile.sheet_names()
            table = excelFile.sheet_by_name("标准告警码")
            r = table.nrows
            e_header = table.row_values(rowx=0, start_colx=0, end_colx=None)
            for i in range(r):
                if i > 0:
                    container.append(table.row_values(rowx=i, start_colx=0, end_colx=None))
        except Exception as e:
            error = error + str(e)
            e_header = None
        return e_header, container, error

