from app.models.user import User
from app.models.transaction import Transaction

class HomeAdminController:

    def __init__(self):
        self.user = User()
        self.transaction = Transaction()

    def showAllTransaction(self):
        return self.transaction.showAll()

    def getNameUser(self):
        return self.user.getName()
    
    