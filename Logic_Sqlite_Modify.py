# -*- coding: utf-8 -*-


class Sqlite_Modify:
    def __init__(self, conn):
        # 创建连接connect, 创建游标cur
        self.connect = conn
        self.cur = self.connect.cursor()

    def sqlite_creat(self, *args, **kwargs):
        """
        *args:用于制作创建表的脚本的表头部分
        **kwargs:用于识别需要创建的表名，格式table=xx
        header是表头字符串，query按标准create table的格式拼接输出语句
        """
        table_head = ",".join("\"" + str(i) + "\"" for i in args[0])
        query_c = """create table if not exists """ + kwargs['table'] + """ (""" + table_head + """)"""
        self.cur.execute(query_c)

    def sqlite_insert(self, i_head, *args, **kwargs):
        """
        *args:需导入的数据
        **kwargs:用于识别需要导入的表名，格式table=xx
        传入需导入的数据，传入类型为列表
        """
        _head = ",".join("\"" + str(s) + "\"" for s in i_head)
        print(_head)
        if _head.find("EUtranCellTDDId") != -1:
            str_head = _head.replace("EUtranCellTDDId", "EUtranCellFDDId") # replace后的原字符串不变，需要赋值给str_head保存
            print(str_head)
        else:
            str_head = _head
        for n, rows in enumerate(args[0]):
            if n > 0:
                try:
                    str_sql = ",".join("\"" + str(i).replace("\"", "'") + "\"" for i in rows)
                    query_i = """insert into """ + kwargs[
                        'table'] + """ (""" + str_head + """) values (""" + str_sql + """)"""
                    self.cur.execute(query_i)
                    # print(query_i)
                except Exception as e:
                    err = ("第%s行出现异常：" + str(e) + "\n插入语句为：\n" + str(rows))
                    return
        self.connect.commit()

    def sqlite_query(self, path=None, operation=None, configure=None, query_Str=None):
        """
        读取写好的sql脚本文件，脚本字符串赋值到query_sql,并返回该字符串
        """
        if operation is None and configure is None:
            with open(path, 'r', encoding='utf8') as file:
                sql_text = file.readlines()
            query_sql = "".join(sql_text)
            self.cur.execute(query_sql)
            result = self.cur.fetchall()
            return result
        elif operation == "delete":
            if configure == "Alarm":
                self.cur.execute("delete from Alarm_State")
                self.cur.execute("delete from Alarm_Cause")
                self.cur.execute("delete from Alarm_syncStatus")
                self.connect.commit()
                self.cur.execute("vacuum")
                # print(result)
            elif configure == "Config_AlarmList":
                self.cur.execute("delete from Config_AlarmList")
                self.connect.commit()
                self.cur.execute("vacuum")
            elif configure == "Config_CellsList":
                self.cur.execute("delete from Config_CellsList")
                self.connect.commit()
                self.cur.execute("vacuum")
            elif configure == "Config_SceneList":
                self.cur.execute("delete from Config_SceneList")
                self.connect.commit()
                self.cur.execute("vacuum")
        elif operation == "update":
            if configure == "Alarm":
                pass
            elif configure == "Carpals":
                pass
        elif operation == "query":
            self.cur.execute(query_Str)
            self.connect.commit()
            result = self.cur.fetchall()
            return result
        else:
            print("error")
            return Exception
