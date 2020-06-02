# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(447, 634)
        MainWindow.setStyleSheet("background-color: #4C4C4C")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.click_button = QtWidgets.QPushButton(self.centralwidget)
        self.click_button.setGeometry(QtCore.QRect(70, 340, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(36)
        self.click_button.setFont(font)
        self.click_button.setStyleSheet("QPushButton {color: #E5D76B ; background-color: #2D2D2D; border: none;}\n"
"QPushButton:hover {color: #EBD84C ; background-color: #3A3A39; border: none;}\n"
"QPushButton:pressed {color: #FFE943 ; background-color: #474746; border: none;}")
        self.click_button.setObjectName("click_button")
        self.upgrade_button = QtWidgets.QPushButton(self.centralwidget)
        self.upgrade_button.setGeometry(QtCore.QRect(120, 430, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(26)
        self.upgrade_button.setFont(font)
        self.upgrade_button.setStyleSheet("QPushButton {color: #ff0000 ; background-color: #2D2D2D; border: none;}")
        self.upgrade_button.setObjectName("upgrade_button")
        self.clicks = QtWidgets.QLabel(self.centralwidget)
        self.clicks.setGeometry(QtCore.QRect(6, 10, 421, 311))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(26)
        self.clicks.setFont(font)
        self.clicks.setTextFormat(QtCore.Qt.AutoText)
        self.clicks.setAlignment(QtCore.Qt.AlignCenter)
        self.clicks.setObjectName("clicks")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(0, 540, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(22)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("QPushButton {color: #37B8B6 ; background-color: #2D2D2D; border: none;}\n"
"QPushButton:hover {color: #42DCDA ; background-color: #3A3A39; border: none;}\n"
"QPushButton:pressed {color: #47F5F2 ; background-color: #474746; border: none;}")
        self.save_button.setObjectName("save_button")
        self.load_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_button.setGeometry(QtCore.QRect(300, 540, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(22)
        self.load_button.setFont(font)
        self.load_button.setStyleSheet("QPushButton {color: #37B8B6 ; background-color: #2D2D2D; border: none;}\n"
"QPushButton:hover {color: #42DCDA ; background-color: #3A3A39; border: none;}\n"
"QPushButton:pressed {color: #47F5F2 ; background-color: #474746; border: none;}")
        self.load_button.setObjectName("load_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 447, 25))
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
        self.click_button.setText(_translate("MainWindow", "Click!"))
        self.upgrade_button.setText(_translate("MainWindow", "Upgrade"))
        self.clicks.setText(_translate("MainWindow", "0"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.load_button.setText(_translate("MainWindow", "Load"))
