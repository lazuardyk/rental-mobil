from app.models.user import User

class EditAccountController:

    def __init__(self, username):
        self.user = User(username)
    
    def getName(self):
        return self.user.getName()
    
    def getEmail(self):
        return self.user.getEmail()
    
    def getAddress(self):
        return self.user.getAddress()
    
    def getPhone(self):
        return self.user.getPhone()
    
    def editAccount(self, name, email, phone, address):
        self.user.setName(name)
        self.user.setEmail(email)
        self.user.setPhone(phone)
        self.user.setAddress(address)