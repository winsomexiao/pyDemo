# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'winsWidget.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Wins_Widget(object):
    def setupUi(self, Wins_Widget):
        Wins_Widget.setObjectName("Wins_Widget")
        Wins_Widget.resize(880, 563)
        self.gridLayoutWidget = QtWidgets.QWidget(Wins_Widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 851, 561))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.mainLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.mainLayout.setObjectName("mainLayout")
        self.bottomLayout = QtWidgets.QHBoxLayout()
        self.bottomLayout.setObjectName("bottomLayout")
        self.leftBottom = QtWidgets.QHBoxLayout()
        self.leftBottom.setObjectName("leftBottom")
        self.progresslable = QtWidgets.QLabel(self.gridLayoutWidget)
        self.progresslable.setObjectName("progresslable")
        self.leftBottom.addWidget(self.progresslable)
        self.progressBar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.leftBottom.addWidget(self.progressBar)
        self.bottomLayout.addLayout(self.leftBottom)
        self.rightBottom = QtWidgets.QHBoxLayout()
        self.rightBottom.setObjectName("rightBottom")
        self.bottomLayout.addLayout(self.rightBottom)
        self.bottomLayout.setStretch(0, 1)
        self.bottomLayout.setStretch(1, 1)
        self.mainLayout.addLayout(self.bottomLayout, 2, 0, 1, 1)
        self.centerLayout = QtWidgets.QHBoxLayout()
        self.centerLayout.setObjectName("centerLayout")
        self.leftLayout = QtWidgets.QVBoxLayout()
        self.leftLayout.setObjectName("leftLayout")
        self.toolBox = QtWidgets.QToolBox(self.gridLayoutWidget)
        self.toolBox.setObjectName("toolBox")
        self.page1 = QtWidgets.QWidget()
        self.page1.setGeometry(QtCore.QRect(0, 0, 82, 409))
        self.page1.setObjectName("page1")
        self.page1group = QtWidgets.QGroupBox(self.page1)
        self.page1group.setGeometry(QtCore.QRect(0, 0, 81, 381))
        self.page1group.setTitle("")
        self.page1group.setObjectName("page1group")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page1group)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, -1, 81, 381))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.page1layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.page1layout.setObjectName("page1layout")
        self.page1btn1 = QtWidgets.QToolButton(self.verticalLayoutWidget_2)
        self.page1btn1.setObjectName("page1btn1")
        self.page1layout.addWidget(self.page1btn1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.page1btn2 = QtWidgets.QToolButton(self.verticalLayoutWidget_2)
        self.page1btn2.setObjectName("page1btn2")
        self.page1layout.addWidget(self.page1btn2, 0, QtCore.Qt.AlignHCenter)
        self.page1btn3 = QtWidgets.QToolButton(self.verticalLayoutWidget_2)
        self.page1btn3.setObjectName("page1btn3")
        self.page1layout.addWidget(self.page1btn3, 0, QtCore.Qt.AlignHCenter)
        self.page1btn4 = QtWidgets.QToolButton(self.verticalLayoutWidget_2)
        self.page1btn4.setObjectName("page1btn4")
        self.page1layout.addWidget(self.page1btn4, 0, QtCore.Qt.AlignHCenter)
        self.page1btn5 = QtWidgets.QToolButton(self.verticalLayoutWidget_2)
        self.page1btn5.setObjectName("page1btn5")
        self.page1layout.addWidget(self.page1btn5, 0, QtCore.Qt.AlignHCenter)
        self.page1btn6 = QtWidgets.QToolButton(self.verticalLayoutWidget_2)
        self.page1btn6.setObjectName("page1btn6")
        self.page1layout.addWidget(self.page1btn6, 0, QtCore.Qt.AlignHCenter)
        self.toolBox.addItem(self.page1, "")
        self.page2 = QtWidgets.QWidget()
        self.page2.setGeometry(QtCore.QRect(0, 0, 82, 409))
        self.page2.setObjectName("page2")
        self.page2group = QtWidgets.QGroupBox(self.page2)
        self.page2group.setGeometry(QtCore.QRect(0, 0, 81, 371))
        self.page2group.setTitle("")
        self.page2group.setObjectName("page2group")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page2group)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 61, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.page2layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.page2layout.setObjectName("page2layout")
        self.page2btn1 = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.page2btn1.setObjectName("page2btn1")
        self.page2layout.addWidget(self.page2btn1, 0, QtCore.Qt.AlignHCenter)
        self.page2btn2 = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.page2btn2.setObjectName("page2btn2")
        self.page2layout.addWidget(self.page2btn2, 0, QtCore.Qt.AlignHCenter)
        self.page2btn3 = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.page2btn3.setObjectName("page2btn3")
        self.page2layout.addWidget(self.page2btn3, 0, QtCore.Qt.AlignHCenter)
        self.page2btn4 = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.page2btn4.setObjectName("page2btn4")
        self.page2layout.addWidget(self.page2btn4, 0, QtCore.Qt.AlignHCenter)
        self.toolBox.addItem(self.page2, "")
        self.leftLayout.addWidget(self.toolBox)
        self.centerLayout.addLayout(self.leftLayout)
        self.rightLayout = QtWidgets.QGridLayout()
        self.rightLayout.setObjectName("rightLayout")
        self.rightGridLayout = QtWidgets.QHBoxLayout()
        self.rightGridLayout.setObjectName("rightGridLayout")
        self.tableView = QtWidgets.QTableView(self.gridLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.rightGridLayout.addWidget(self.tableView)
        self.rightLayout.addLayout(self.rightGridLayout, 1, 0, 1, 1)
        self.rightBtnsLayout = QtWidgets.QHBoxLayout()
        self.rightBtnsLayout.setObjectName("rightBtnsLayout")
        self.qryBtn = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.qryBtn.setObjectName("qryBtn")
        self.rightBtnsLayout.addWidget(self.qryBtn)
        self.addBtn = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.addBtn.setObjectName("addBtn")
        self.rightBtnsLayout.addWidget(self.addBtn)
        self.delBtn = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.delBtn.setObjectName("delBtn")
        self.rightBtnsLayout.addWidget(self.delBtn)
        self.rightLayout.addLayout(self.rightBtnsLayout, 0, 0, 1, 1)
        self.rightLayout.setRowStretch(0, 1)
        self.rightLayout.setRowStretch(1, 9)
        self.centerLayout.addLayout(self.rightLayout)
        self.centerLayout.setStretch(0, 1)
        self.centerLayout.setStretch(1, 9)
        self.mainLayout.addLayout(self.centerLayout, 1, 0, 1, 1)
        self.topLayout = QtWidgets.QHBoxLayout()
        self.topLayout.setObjectName("topLayout")
        self.headIcon = QtWidgets.QLabel(self.gridLayoutWidget)
        self.headIcon.setObjectName("headIcon")
        self.topLayout.addWidget(self.headIcon)
        self.headTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        self.headTitle.setObjectName("headTitle")
        self.topLayout.addWidget(self.headTitle)
        self.searchInput = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.searchInput.setObjectName("searchInput")
        self.topLayout.addWidget(self.searchInput)
        self.searchBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.searchBtn.setObjectName("searchBtn")
        self.topLayout.addWidget(self.searchBtn)
        self.topSpace = QtWidgets.QLabel(self.gridLayoutWidget)
        self.topSpace.setObjectName("topSpace")
        self.topLayout.addWidget(self.topSpace)
        self.loginBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.loginBtn.setObjectName("loginBtn")
        self.topLayout.addWidget(self.loginBtn)
        self.minBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.minBtn.setObjectName("minBtn")
        self.topLayout.addWidget(self.minBtn)
        self.maxBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.maxBtn.setObjectName("maxBtn")
        self.topLayout.addWidget(self.maxBtn)
        self.closeBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.closeBtn.setObjectName("closeBtn")
        self.topLayout.addWidget(self.closeBtn)
        self.topLayout.setStretch(0, 2)
        self.topLayout.setStretch(1, 2)
        self.topLayout.setStretch(2, 3)
        self.topLayout.setStretch(3, 1)
        self.topLayout.setStretch(4, 10)
        self.topLayout.setStretch(5, 1)
        self.topLayout.setStretch(6, 1)
        self.topLayout.setStretch(7, 1)
        self.topLayout.setStretch(8, 1)
        self.mainLayout.addLayout(self.topLayout, 0, 0, 1, 1)
        self.mainLayout.setRowStretch(0, 2)
        self.mainLayout.setRowStretch(1, 17)
        self.mainLayout.setRowStretch(2, 1)

        self.retranslateUi(Wins_Widget)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Wins_Widget)

    def retranslateUi(self, Wins_Widget):
        _translate = QtCore.QCoreApplication.translate
        Wins_Widget.setWindowTitle(_translate("Wins_Widget", "Form"))
        self.progresslable.setText(_translate("Wins_Widget", "加载进度:"))
        self.page1btn1.setText(_translate("Wins_Widget", "1-1"))
        self.page1btn2.setText(_translate("Wins_Widget", "1-2"))
        self.page1btn3.setText(_translate("Wins_Widget", "1-3"))
        self.page1btn4.setText(_translate("Wins_Widget", "1-4"))
        self.page1btn5.setText(_translate("Wins_Widget", "1-5"))
        self.page1btn6.setText(_translate("Wins_Widget", "1-6"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page1), _translate("Wins_Widget", "个人账务"))
        self.page2btn1.setText(_translate("Wins_Widget", "2-1"))
        self.page2btn2.setText(_translate("Wins_Widget", "2-2"))
        self.page2btn3.setText(_translate("Wins_Widget", "2-3"))
        self.page2btn4.setText(_translate("Wins_Widget", "2-4"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page2), _translate("Wins_Widget", "数据采集"))
        self.qryBtn.setText(_translate("Wins_Widget", "qryBtn"))
        self.addBtn.setText(_translate("Wins_Widget", "addBtn"))
        self.delBtn.setText(_translate("Wins_Widget", "delBtn"))
        self.headIcon.setText(_translate("Wins_Widget", "HeadIcon"))
        self.headTitle.setText(_translate("Wins_Widget", "HeadTitle"))
        self.searchBtn.setText(_translate("Wins_Widget", "PushButton"))
        self.topSpace.setText(_translate("Wins_Widget", "TextLabel"))
        self.loginBtn.setText(_translate("Wins_Widget", "PushButton"))
        self.minBtn.setText(_translate("Wins_Widget", "PushButton"))
        self.maxBtn.setText(_translate("Wins_Widget", "PushButton"))
        self.closeBtn.setText(_translate("Wins_Widget", "PushButton"))

