from PyQt5 import QtCore, QtGui, QtWidgets
from app.controllers.managecarcontroller import ManageCarController
# from app.views.homeuser import HomeUser_Window
import locale

class ManageCar_Window(object):
    def __init__(self, callback=None):
        if callback:
            self.callback = callback
        self.carcontroller = ManageCarController()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.show()
        
    def setupUi(self, MainWindow):
        self.allcar = self.carcontroller.showAllCar()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(858, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 380, 191, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 430, 101, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(400, 460, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 430, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(700, 430, 81, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(560, 460, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(700, 460, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 490, 101, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(400, 520, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(560, 490, 121, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(560, 520, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(560, 550, 111, 41))
        self.pushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 20, 121, 41))
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(90, 70, 671, 291))
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(len(self.allcar))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
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
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(109)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(80, 380, 181, 41))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 430, 101, 16))
        self.label_9.setObjectName("label_9")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 550, 111, 41))
        self.pushButton_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 460, 121, 31))
        self.comboBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(190, 430, 101, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(190, 480, 101, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(190, 450, 71, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(190, 500, 71, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(700, 490, 131, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(700, 520, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def rupiah_format(self, angka):
        desimal = 2
        locale.setlocale(locale.LC_NUMERIC, 'IND')
        rupiah = locale.format("%.*f", (desimal, angka), True)
        return "Rp{}".format(rupiah)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rental Mobil - Kelola Mobil"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Form Tambah Mobil</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Merek Mobil:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Model Mobil:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Nomor Polisi:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Warna:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Tahun Pembuatan:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Tambah"))
        self.pushButton.clicked.connect(self.pushAddCar)
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Daftar Mobil</span></p></body></html>"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Merek Mobil"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Model Mobil"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nomor Polisi"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Warna"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tahun Pembuatan"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Harga Sewa Per Hari"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        # print(self.allcar)
        for i in range(len(self.allcar)):
            count = 0
            for key, value in self.allcar[i].items():
                # print(key, value)
                if key == "_id":
                    continue
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(i, count, item)
                item = self.tableWidget.item(i, count)
                if key == "price_per_day":
                    item.setText(_translate("MainWindow", self.rupiah_format(value)))
                else:
                    item.setText(_translate("MainWindow", str(value)))
                count += 1
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Form Hapus Mobil</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Nomor Polisi:</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Hapus"))
        self.pushButton_3.clicked.connect(self.pushDeleteCar)
        self.list_plat = self.carcontroller.showAllPlatCar()
        
        if len(self.allcar) > 0:
            for key, value in self.allcar[0].items():
                if key == "_id":
                    self.id_car = value

        index_plat = 0
        for i in self.list_plat:
            self.comboBox.addItem("")
            for key, value in i.items():
                self.comboBox.setItemText(index_plat, _translate("MainWindow", key))
            index_plat += 1
        # self.comboBox.setItemText(0, _translate("MainWindow", "B 123 K"))
        self.comboBox.currentIndexChanged.connect(self.platComboChanged)
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Merek Mobil:</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Model Mobil:</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Toyota</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Avanza</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Harga Sewa Per Hari:</span></p></body></html>"))

    def pushAddCar(self):
        brand = self.lineEdit.text()
        color = self.lineEdit_4.text()
        model = self.lineEdit_2.text()
        production_year = self.lineEdit_5.text()
        license_plate = self.lineEdit_3.text()
        price = int(self.lineEdit_6.text())
        self.carcontroller.addCar(brand, model, color, license_plate, price, production_year)
        self.MainWindow.close()
        self.popupSuccess()
    
    def platComboChanged(self, value):
        # self.list_plat = self.carcontroller.showAllPlatCar()
        plat_dict = self.list_plat[value]
        for key, value in plat_dict.items():
            self.id_car = value
            id_plat = value
        _translate = QtCore.QCoreApplication.translate
        brand = self.carcontroller.getBrandCar(id_plat)
        model = self.carcontroller.getModelCar(id_plat)
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">"+brand+"</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">"+model+"</span></p></body></html>"))
    
    def pushDeleteCar(self):
        self.carcontroller.deleteCar(self.id_car)
        self.MainWindow.close()
        self.popupSuccess()
    
    def popupSuccess(self):
        if self.callback:
            self.callback.refreshHome()
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Rental Mobil - Success")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Sukses!")
        msg.exec_()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.show()

