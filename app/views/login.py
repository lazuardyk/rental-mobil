from app.controllers.logincontroller import LoginController
from app.views.homeuser import HomeUser_Window
from app.views.homeadmin import HomeAdmin_Window
from PyQt5 import QtCore, QtGui, QtWidgets

class Login_Window(object):

    def __init__(self):
        MainWindow = QtWidgets.QMainWindow()
        self.setupUi(MainWindow)
        MainWindow.show()
 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 446)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 391, 191))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 240, 81, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 240, 121, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 280, 81, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 280, 121, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 340, 91, 31))
        self.pushButton.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rental Mobil - Login"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/rental logo.jpg\"/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Username:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Password:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.pushButton.clicked.connect(lambda: self.pushLogin(MainWindow))
    
    def pushLogin(self, MainWindow):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        login_controller = LoginController(username, password)
        if login_controller.checkLogin():
            if login_controller.checkRole() == "user":
                self.homeuser = HomeUser_Window(username)
            else:
                self.homeadmin = HomeAdmin_Window(username)
            MainWindow.close()
        else:
            self.popupWrongLogin()

    def popupWrongLogin(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Rental Mobil - Alert")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Username atau password salah!")
        msg.exec_()


import app.views.logo_rc
