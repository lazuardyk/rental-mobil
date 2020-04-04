from app.views.login import Login_Window
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Main:
    
    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        login = Login_Window()
        sys.exit(app.exec_())