# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import threading

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.my233 = QtWidgets.QLabel(self.centralwidget)
        self.my233.setGeometry(QtCore.QRect(20, 20, 54, 12))
        self.my233.setObjectName("my233")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(410, 110, 160, 22))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setPageStep(10)
        self.horizontalSlider.setProperty("value", 1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.my233.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.clicked.connect(self.zero)

    def zero(self):
        global i
        i = 0
        global timer
        if timer:
            timer.cancel()
        self.fun()

    def fun(self):
        global i
        self.my233.setText(str(i))
        print(i)
        i += 1
        n = self.horizontalSlider.value()
        global timer
        timer = threading.Timer(1 / n, self.fun)
        timer.start()

    def closeEvent(self, event):
        global timer
        timer.cancel()
        reply = QtWidgets.QMessageBox.question(self, 'Message',
                                               'Are you sure to quit?', QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    import sys
    import time

    timer = None
    i = 0
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
