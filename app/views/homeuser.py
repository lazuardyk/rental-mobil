from PyQt5 import QtCore, QtGui, QtWidgets
from app.views.managecar import ManageCar_Window
from app.views.editaccount import EditAccount_Window
from app.controllers.homeusercontroller import HomeUserController
import locale

class HomeUser_Window(object):

    def __init__(self, username):
        self.username = username
        self.homeusercontroller = HomeUserController(self.username)
        self.name = self.homeusercontroller.getNameUser()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.show()

    def setupUi(self, MainWindow):
        self.duration = 1
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 597)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 120, 141, 61))
        self.pushButton.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 60, 371, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 120, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 150, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 210, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 270, 81, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 330, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 120, 151, 21))
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(200, 370, 141, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(200, 440, 81, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(200, 490, 171, 20))
        self.label_12.setObjectName("label_12")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, 400, 69, 22))
        self.comboBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setGeometry(QtCore.QRect(200, 520, 141, 31))
        self.dateEdit.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(410, 180, 201, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(410, 240, 201, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setGeometry(QtCore.QRect(410, 300, 201, 22))
        self.dateEdit_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(410, 360, 201, 21))
        self.lineEdit_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(200, 460, 181, 20))
        self.label_13.setObjectName("label_13")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 220, 81, 20))
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 520, 171, 41))
        self.pushButton_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 50, 131, 31))
        self.pushButton_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(410, 390, 47, 13))
        self.label_9.setObjectName("label_9")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 20, 341, 31))
        self.label_14.setObjectName("label_14")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(410, 420, 201, 91))
        self.textEdit.setObjectName("textEdit")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(200, 150, 121, 20))
        self.label_15.setObjectName("label_15")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(200, 180, 141, 31))
        self.comboBox_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.comboBox_3.setObjectName("comboBox_3")
        
        # self.comboBox_3.addItem("")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(200, 320, 91, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(200, 240, 101, 20))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(200, 340, 91, 20))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(200, 290, 101, 20))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(200, 270, 81, 20))
        self.label_20.setObjectName("label_20")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rental Mobil - Form Pemesanan"))
        self.pushButton.setText(_translate("MainWindow", "Kelola Data Mobil"))
        self.pushButton.clicked.connect(self.pushManageCar)
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Form Pemesanan Rental Mobil</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Data Pelanggan</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Nama:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Nomor KTP:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Tanggal Lahir:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Nomor HP:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Informasi Peminjaman</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Durasi Peminjaman:</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Harga:</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Tanggal Peminjaman:</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1 hari"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2 hari"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3 hari"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4 hari"))
        self.comboBox.setItemText(4, _translate("MainWindow", "5 hari"))
        self.comboBox.setItemText(5, _translate("MainWindow", "6 hari"))
        self.comboBox.setItemText(6, _translate("MainWindow", "7 hari"))
        self.comboBox.currentIndexChanged.connect(self.durationComboChanged)
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Merek Mobil:</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Submit Data"))
        self.pushButton_2.clicked.connect(self.pushAddTransaction)
        self.pushButton_3.setText(_translate("MainWindow", "Edit Informasi Akun"))
        self.pushButton_3.clicked.connect(self.pushEditAccount)
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Alamat:</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Selamat Datang, "+self.name+" (User)</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Pilih No Polisi Mobil:</span></p></body></html>"))

        self.list_plat = self.homeusercontroller.showAllPlatCar()
        index_plat = 0
        for i in self.list_plat:
            self.comboBox_3.addItem("")
            for key, value in i.items():
                self.comboBox_3.setItemText(index_plat, _translate("MainWindow", key))
            index_plat += 1
        self.comboBox_3.currentIndexChanged.connect(self.platComboChanged)
        if len(self.list_plat) != 0:
            plat_dict = self.list_plat[0]
            for key, value in plat_dict.items():
                self.id_car = value
                id_plat = value
            brand = self.homeusercontroller.getBrandCar(id_plat)
            model = self.homeusercontroller.getModelCar(id_plat)
            color = self.homeusercontroller.getColorCar(id_plat)
            self.pricecar_int = self.homeusercontroller.getPriceCar(id_plat)
            self.price_total = self.pricecar_int
            price = self.rupiah_format(self.pricecar_int)
            self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">"+brand+"</span></p></body></html>"))
            self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">"+color+"</span></p></body></html>"))
            self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">"+model+"</span></p></body></html>"))
            self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">"+price+"</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Warna Mobil:</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Model Mobil:</span></p></body></html>"))

    def pushManageCar(self):
        self.managecar = ManageCar_Window()
    
    def pushEditAccount(self):
        self.editaccount = EditAccount_Window(self.username)

    def rupiah_format(self, angka):
        desimal = 2
        locale.setlocale(locale.LC_NUMERIC, 'IND')
        rupiah = locale.format("%.*f", (desimal, angka), True)
        return "Rp{}".format(rupiah)

    def pushAddTransaction(self):
        buyer_name = self.lineEdit_4.text()
        buyer_ktp = self.lineEdit_5.text()
        buyer_birthday = self.dateEdit_2.date().toPyDate().strftime("%d-%m-%Y")
        date_buy_py = self.dateEdit.date().toPyDate()
        date_buy = date_buy_py.strftime("%d-%m-%Y")
        buyer_hp = self.lineEdit_6.text()
        buyer_address = self.textEdit.toPlainText()
        self.homeusercontroller.addTransaction(self.id_car, self.duration, buyer_name,buyer_address,buyer_hp,buyer_ktp,self.pricecar_int)
        self.MainWindow.close()
        self.popupSuccess()
    
    def popupSuccess(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Rental Mobil - Success")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Sukses!")
        msg.exec_()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.show()

    def platComboChanged(self, value):
        plat_dict = self.list_plat[value]
        for key, value in plat_dict.items():
            self.id_car = value
            id_plat = value
        _translate = QtCore.QCoreApplication.translate
        brand = self.homeusercontroller.getBrandCar(id_plat)
        model = self.homeusercontroller.getModelCar(id_plat)
        color = self.homeusercontroller.getColorCar(id_plat)
        self.pricecar_int = self.homeusercontroller.getPriceCar(id_plat)
        price = self.rupiah_format(self.pricecar_int)
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">"+brand+"</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">"+color+"</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">"+model+"</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">"+price+"</span></p></body></html>"))
    
    def durationComboChanged(self, value):
        _translate = QtCore.QCoreApplication.translate
        self.duration = value+1
        self.price_total = self.pricecar_int * self.duration
        price = self.rupiah_format(self.price_total)
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">"+price+"</span></p></body></html>"))