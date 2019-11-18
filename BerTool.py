# -*- coding: utf-8 -*-

import os
import sys
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from GUI_SignalContrl import *
from GUI_Dialog import *

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_signalContrl()
    try:
        ui.setupUi(mainWindow)
        ui.alarm_setupUi()
        ui.AlarmConfig_setupUi()
        ui.QtWidget_Function()
        mainWindow.show()
        sys.exit(app.exec_())
    except Exception as e:
        ui.QMessageBoxShow("主窗口错误", str(e), 0)
