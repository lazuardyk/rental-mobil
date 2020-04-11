from PyQt5 import QtCore, QtGui, QtWidgets
from app.views.managecar import ManageCar_Window
from app.views.manageuser import ManageUser_Window
from app.views.manageadmin import ManageAdmin_Window
from app.views.editaccount import EditAccount_Window
from app.controllers.homeadmincontroller import HomeAdminController
import locale

class HomeAdmin_Window(object):

    def __init__(self, username):
        self.username = username
        self.admincontroller = HomeAdminController(username)
        self.name = self.admincontroller.getNameUser()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.show()

    def setupUi(self, MainWindow):
        self.alltransaction = self.admincontroller.showAllTransaction()
        self.tabledata = self.admincontroller.showTableData()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1184, 522)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 20, 341, 31))
        self.label_14.setObjectName("label_14")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 80, 161, 21))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 120, 1161, 192))
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(len(self.tabledata))
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(115)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 330, 231, 61))
        self.pushButton.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 330, 221, 61))
        self.pushButton_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 420, 221, 61))
        self.pushButton_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 340, 221, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 410, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 380, 101, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 440, 111, 41))
        self.pushButton_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 50, 151, 31))
        self.pushButton_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rental Mobil - Admin"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Selamat Datang, Lazuardy Khatulistiwa (Admin)</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Riwayat Transaksi</span></p></body></html>"))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item.setText(_translate("MainWindow", "Tgl Peminjaman"))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item.setText(_translate("MainWindow", "Nama Pelanggan"))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item.setText(_translate("MainWindow", "No HP"))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item.setText(_translate("MainWindow", "No KTP"))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item.setText(_translate("MainWindow", "Alamat"))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item.setText(_translate("MainWindow", "Merek Mobil"))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item.setText(_translate("MainWindow", "Model Mobil"))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item.setText(_translate("MainWindow", "No Polisi"))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item.setText(_translate("MainWindow", "Durasi"))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item.setText(_translate("MainWindow", "Total Harga"))
        for i in range(len(self.tabledata)):
            count = 0
            for key, value in self.tabledata[i].items():
                # print(key, value)
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                if key == "rent_date":
                    self.tableWidget.setItem(i, 0, item)
                    item = self.tableWidget.item(i, 0)
                elif key == "buyer_name":
                    self.tableWidget.setItem(i, 1, item)
                    item = self.tableWidget.item(i, 1)
                elif key == "buyer_phone":
                    self.tableWidget.setItem(i, 2, item)
                    item = self.tableWidget.item(i, 2)
                elif key == "buyer_idcard":
                    self.tableWidget.setItem(i, 3, item)
                    item = self.tableWidget.item(i, 3)
                elif key == "buyer_address":
                    self.tableWidget.setItem(i, 4, item)
                    item = self.tableWidget.item(i, 4)
                elif key == "car_brand":
                    self.tableWidget.setItem(i, 5, item)
                    item = self.tableWidget.item(i, 5)
                elif key == "car_model":
                    self.tableWidget.setItem(i, 6, item)
                    item = self.tableWidget.item(i, 6)
                elif key == "license_plate":
                    self.tableWidget.setItem(i, 7, item)
                    item = self.tableWidget.item(i, 7)
                elif key == "duration":
                    self.tableWidget.setItem(i, 8, item)
                    item = self.tableWidget.item(i, 8)
                else:
                    self.tableWidget.setItem(i, 9, item)
                    item = self.tableWidget.item(i, 9)
                if key == "price_total":
                    item.setText(_translate("MainWindow", self.rupiah_format(value)))
                elif key == "duration":
                    item.setText(_translate("MainWindow", str(value)+" hari"))
                else:
                    item.setText(_translate("MainWindow", str(value)))
                count += 1
        self.pushButton.setText(_translate("MainWindow", "Kelola Data Mobil"))
        self.pushButton.clicked.connect(self.pushManageCar)
        self.pushButton_2.setText(_translate("MainWindow", "Kelola Data User"))
        self.pushButton_2.clicked.connect(self.pushManageUser)
        self.pushButton_3.setText(_translate("MainWindow", "Kelola Data Admin"))
        self.pushButton_3.clicked.connect(self.pushManageAdmin)
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Form Hapus Transaksi</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Nomor Transaksi:</span></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "Hapus"))
        self.pushButton_4.clicked.connect(self.pushDeleteTransaction)
        self.pushButton_5.setText(_translate("MainWindow", "Edit Informasi Akun"))
        self.pushButton_5.clicked.connect(self.pushEditAccount)

    def pushManageCar(self):
        self.managecar = ManageCar_Window()
    
    def pushManageUser(self):
        self.manageuser = ManageUser_Window()
    
    def pushManageAdmin(self):
        self.manageadmin = ManageAdmin_Window()
    
    def pushEditAccount(self):
        self.editaccount = EditAccount_Window(self.username)
    
    def rupiah_format(self, angka):
        desimal = 2
        locale.setlocale(locale.LC_NUMERIC, 'IND')
        rupiah = locale.format("%.*f", (desimal, angka), True)
        return "Rp{}".format(rupiah)
    
    def pushDeleteTransaction(self):
        no_transaksi = self.lineEdit.text()
        self.admincontroller.deleteTransaction(no_transaksi)
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
