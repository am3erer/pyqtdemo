# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuWindow.ui'
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setObjectName("menuOpen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionN = QtWidgets.QAction(MainWindow)
        self.actionN.setCheckable(True)
        self.actionN.setObjectName("actionN")
        self.actioncsv = QtWidgets.QAction(MainWindow)
        self.actioncsv.setObjectName("actioncsv")
        self.menuOpen.addAction(self.actioncsv)
        self.menuFile.addAction(self.actionN)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionN)
        self.toolBar.addAction(self.actioncsv)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionN.setText(_translate("MainWindow", "New"))
        self.actioncsv.setText(_translate("MainWindow", "csv"))

