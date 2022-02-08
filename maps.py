import sys
from io import BytesIO

import requests
from PIL import Image, ImageQt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

global_coords = ""
global_scale = ""
server = "https://static-maps.yandex.ru/1.x/"
map_params = {"ll": global_coords, "l": "map", "spn": global_scale}


class Maps_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(749, 663)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.coords_line = QtWidgets.QLineEdit(self.centralwidget)
        self.coords_line.setGeometry(QtCore.QRect(130, 40, 471, 31))
        self.coords_line.setObjectName("coords_line")
        self.scale_line = QtWidgets.QLineEdit(self.centralwidget)
        self.scale_line.setGeometry(QtCore.QRect(130, 90, 471, 31))
        self.scale_line.setObjectName("scale_line")
        self.show_map_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_map_btn.setGeometry(QtCore.QRect(320, 140, 101, 31))
        self.show_map_btn.setObjectName("show_map_btn")
        self.show_map_btn.clicked.connect(self.show_map)
        self.coords_label = QtWidgets.QLabel(self.centralwidget)
        self.coords_label.setGeometry(QtCore.QRect(40, 40, 71, 31))
        self.coords_label.setObjectName("coords_label")
        self.scale_label = QtWidgets.QLabel(self.centralwidget)
        self.scale_label.setGeometry(QtCore.QRect(50, 90, 71, 31))
        self.scale_label.setObjectName("scale_label")
        self.picture_label = QtWidgets.QLabel(self.centralwidget)
        self.picture_label.setGeometry(QtCore.QRect(160, 200, 421, 401))
        self.picture_label.setText("")
        self.picture_label.setObjectName("picture_label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(630, 40, 91, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scheme = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.scheme.setObjectName("scheme")
        self.verticalLayout.addWidget(self.scheme)
        self.satellite = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.satellite.setObjectName("satellite")
        self.verticalLayout.addWidget(self.satellite)
        self.hybrid = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.hybrid.setObjectName("hybrid")
        self.verticalLayout.addWidget(self.hybrid)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 749, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Карта"))
        self.show_map_btn.setText(_translate("MainWindow", "Показать карту"))
        self.coords_label.setText(_translate("MainWindow", "Координаты:"))
        self.scale_label.setText(_translate("MainWindow", "Масштаб:"))
        self.scheme.setText(_translate("MainWindow", "Схема"))
        self.satellite.setText(_translate("MainWindow", "Спутник"))
        self.hybrid.setText(_translate("MainWindow", "Гибрид"))

    def get_coords(self):
        return self.coords_line.text()

    def get_scale(self):
        return self.scale_line.text()

    def get_layer(self):
        if self.satellite.isChecked():
            return 'sat'
        elif self.hybrid.isChecked():
            return 'sat,skl'
        return 'map'

    def show_map(self):
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={self.get_coords()}&" \
                      f"spn={self.get_scale()}&l={self.get_layer()}"
        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        self.image = ImageQt.ImageQt(Image.open(BytesIO(response.content)))
        self.picture_label.setPixmap(QPixmap.fromImage(self.image))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Maps_Window()
    ex.show()
    sys.exit(app.exec_())

# 37.677751,55.757718
# 0.003,0.003
