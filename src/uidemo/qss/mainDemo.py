#! /usr/bin/env python
# -*- coding: utf-8 -*-


import signal

from src.uidemo.qss.winswidgetDemo import WinsWidget

signal.signal(signal.SIGINT, signal.SIG_DFL)

import logging
logging.basicConfig(level=logging.INFO) # change to 'DEBUG' to see more

from PyQt5 import QtWidgets, QtGui

def setFontFamily(font):
    allFamillies = QtGui.QFontDatabase().families()
    familyName = font.defaultFamily()  
    if "微软雅黑" in allFamillies:
        familyName = "微软雅黑"
    font.setFamily(familyName)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    font = QtGui.QFont()
    setFontFamily(font)
    font.setPixelSize(14)
    app.setFont(font)
    win = WinsWidget()
    win.show()
    sys.exit(app.exec_())

