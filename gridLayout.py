# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gridLayout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 140, 356, 165))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 0, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_2.addWidget(self.pushButton_13, 0, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_2.addWidget(self.pushButton_14, 0, 2, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 1, 0, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_2.addWidget(self.pushButton_16, 1, 1, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_2.addWidget(self.pushButton_17, 1, 2, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_2.addWidget(self.pushButton_18, 2, 0, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_2.addWidget(self.pushButton_19, 2, 1, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_2.addWidget(self.pushButton_20, 2, 2, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_2.addWidget(self.pushButton_21, 3, 2, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_2.addWidget(self.pushButton_22, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_12.setText(_translate("MainWindow", "7"))
        self.pushButton_13.setText(_translate("MainWindow", "8"))
        self.pushButton_14.setText(_translate("MainWindow", "9"))
        self.pushButton_15.setText(_translate("MainWindow", "4"))
        self.pushButton_16.setText(_translate("MainWindow", "5"))
        self.pushButton_17.setText(_translate("MainWindow", "6"))
        self.pushButton_18.setText(_translate("MainWindow", "1"))
        self.pushButton_19.setText(_translate("MainWindow", "2"))
        self.pushButton_20.setText(_translate("MainWindow", "3"))
        self.pushButton_21.setText(_translate("MainWindow", "."))
        self.pushButton_22.setText(_translate("MainWindow", "0"))

