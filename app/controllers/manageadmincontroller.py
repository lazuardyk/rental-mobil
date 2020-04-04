from app.models.user import User

class ManageAdminController:

    def __init__(self):
        self.user = User()
    
    def showAllAdmin(self):
        alladmin = []
        alluser = self.user.showAll()
        for i in alluser:
            if i['role'] == 'admin':
                alladmin.append(i)
        return alladmin

    def addAdmin(self, name, address, email, username, password):
        role = 'admin'
        return self.user.add(name, address, email, username, password, role)
    
    def deleteAdmin(self, username):
        u = User(username)
        u.deleteThisUser()
    
    
