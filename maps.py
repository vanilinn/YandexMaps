import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Maps_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(752, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.picture_label = QtWidgets.QLabel(self.centralwidget)
        self.picture_label.setGeometry(QtCore.QRect(200, 200, 321, 301))
        self.picture_label.setObjectName("picture_label")
        self.coords_line = QtWidgets.QLineEdit(self.centralwidget)
        self.coords_line.setGeometry(QtCore.QRect(160, 40, 521, 31))
        self.coords_line.setObjectName("coords_line")
        self.scale_line = QtWidgets.QLineEdit(self.centralwidget)
        self.scale_line.setGeometry(QtCore.QRect(160, 90, 521, 31))
        self.scale_line.setObjectName("scale_line")
        self.coords_btn = QtWidgets.QPushButton(self.centralwidget)
        self.coords_btn.setGeometry(QtCore.QRect(50, 40, 91, 31))
        self.coords_btn.setObjectName("coords_btn")
        self.scale_btn = QtWidgets.QPushButton(self.centralwidget)
        self.scale_btn.setGeometry(QtCore.QRect(50, 90, 91, 31))
        self.scale_btn.setObjectName("scale_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 752, 21))
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
        self.picture_label.setText(_translate("MainWindow", "TextLabel"))
        self.coords_btn.setText(_translate("MainWindow", "Координаты:"))
        self.scale_btn.setText(_translate("MainWindow", "Масштаб:"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Maps_Window()
    ex.show()
    sys.exit(app.exec_())
