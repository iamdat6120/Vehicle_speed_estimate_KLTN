# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1381, 855)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1381, 831))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.groupBox = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox.setGeometry(QtCore.QRect(1160, 220, 201, 571))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 30, 171, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_fps = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_fps.setFont(font)
        self.label_fps.setObjectName("label_fps")
        self.horizontalLayout_4.addWidget(self.label_fps)
        self.label_value_fps = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_value_fps.setFont(font)
        self.label_value_fps.setObjectName("label_value_fps")
        self.horizontalLayout_4.addWidget(self.label_value_fps)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 90, 171, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_total = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_total.setFont(font)
        self.label_total.setObjectName("label_total")
        self.horizontalLayout_5.addWidget(self.label_total)
        self.label_value_total = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_value_total.setFont(font)
        self.label_value_total.setObjectName("label_value_total")
        self.horizontalLayout_5.addWidget(self.label_value_total)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 160, 171, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_in_red_place = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_in_red_place.setFont(font)
        self.label_in_red_place.setObjectName("label_in_red_place")
        self.horizontalLayout_6.addWidget(self.label_in_red_place)
        self.label_value_in_red_place = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_value_in_red_place.setFont(font)
        self.label_value_in_red_place.setObjectName("label_value_in_red_place")
        self.horizontalLayout_6.addWidget(self.label_value_in_red_place)
        self.lblHost = QtWidgets.QLabel(self.groupBox)
        self.lblHost.setGeometry(QtCore.QRect(10, 260, 31, 31))
        self.lblHost.setObjectName("lblHost")
        self.lblPort = QtWidgets.QLabel(self.groupBox)
        self.lblPort.setGeometry(QtCore.QRect(10, 320, 47, 31))
        self.lblPort.setObjectName("lblPort")
        self.txtHost = QtWidgets.QTextEdit(self.groupBox)
        self.txtHost.setGeometry(QtCore.QRect(40, 260, 141, 31))
        self.txtHost.setObjectName("txtHost")
        self.txtPort = QtWidgets.QTextEdit(self.groupBox)
        self.txtPort.setGeometry(QtCore.QRect(70, 320, 111, 31))
        self.txtPort.setObjectName("txtPort")
        self.ptnGo = QtWidgets.QPushButton(self.groupBox)
        self.ptnGo.setGeometry(QtCore.QRect(60, 380, 75, 23))
        self.ptnGo.setObjectName("ptnGo")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(1170, 10, 191, 80))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_date = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.horizontalLayout.addWidget(self.label_date)
        self.label_value_date = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_value_date.setFont(font)
        self.label_value_date.setObjectName("label_value_date")
        self.horizontalLayout.addWidget(self.label_value_date)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_time = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")
        self.horizontalLayout_3.addWidget(self.label_time)
        self.label_value_time = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_value_time.setFont(font)
        self.label_value_time.setObjectName("label_value_time")
        self.horizontalLayout_3.addWidget(self.label_value_time)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1170, 100, 191, 107))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.checkBox_deadline = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_deadline.setObjectName("checkBox_deadline")
        self.verticalLayout.addWidget(self.checkBox_deadline)
        self.checkBox_bb = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_bb.setObjectName("checkBox_bb")
        self.verticalLayout.addWidget(self.checkBox_bb)
        self.checkBox_area = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_area.setObjectName("checkBox_area")
        self.verticalLayout.addWidget(self.checkBox_area)
        self.checkBox_his = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_his.setObjectName("checkBox_his")
        self.verticalLayout.addWidget(self.checkBox_his)
        self.lbl_Image = QtWidgets.QLabel(self.tab_5)
        self.lbl_Image.setGeometry(QtCore.QRect(0, 10, 1161, 781))
        self.lbl_Image.setText("")
        self.lbl_Image.setObjectName("lbl_Image")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1361, 741))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.btn_reload = QtWidgets.QPushButton(self.tab_6)
        self.btn_reload.setGeometry(QtCore.QRect(1250, 760, 111, 31))
        self.btn_reload.setObjectName("btn_reload")
        self.tabWidget.addTab(self.tab_6, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1381, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Details"))
        self.label_fps.setText(_translate("MainWindow", "FPS:"))
        self.label_value_fps.setText(_translate("MainWindow", "-"))
        self.label_total.setText(_translate("MainWindow", "Total vehicle: "))
        self.label_value_total.setText(_translate("MainWindow", "-"))
        self.label_in_red_place.setText(_translate("MainWindow", "In red place: "))
        self.label_value_in_red_place.setText(_translate("MainWindow", "-"))
        self.lblHost.setText(_translate("MainWindow", "Host:"))
        self.lblPort.setText(_translate("MainWindow", "Port:"))
        self.ptnGo.setText(_translate("MainWindow", "Go!!!"))
        self.label_date.setText(_translate("MainWindow", "Date: "))
        self.label_value_date.setText(_translate("MainWindow", "-"))
        self.label_time.setText(_translate("MainWindow", "Time: "))
        self.label_value_time.setText(_translate("MainWindow", "-"))
        self.label.setText(_translate("MainWindow", "L???a ch???n hi???n th???"))
        self.checkBox_deadline.setText(_translate("MainWindow", "Hi???n th??? v???ch d???ng ????n ?????"))
        self.checkBox_bb.setText(_translate("MainWindow", "Hi???n th??? bounding box"))
        self.checkBox_area.setText(_translate("MainWindow", "Hi???n th??? khu v???c detection"))
        self.checkBox_his.setText(_translate("MainWindow", "Hi???n th??? l???ch s??? di chuy???n "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Tab 1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Lo???i ph????ng ti???n"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Lo???i t???i ph???m    "))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "V???n t???c"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Bi???n s??? xe"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Th???i gian"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "H??nh ???nh"))
        self.btn_reload.setText(_translate("MainWindow", "Reload"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
