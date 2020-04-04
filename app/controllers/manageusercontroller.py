from app.models.user import User

class ManageUserController:

    def __init__(self):
        self.user = User()
    
    def showAllUser(self):
        all_user = []
        alluser = self.user.showAll()
        for i in alluser:
            if i['role'] == 'user':
                all_user.append(i)
        return all_user

    def addUser(self, name, address, email, username, password):
        role = 'user'
        return self.user.add(name, address, email, username, password, role)
    
    def deleteUser(self, username):
        u = User(username)
        u.deleteThisUser()
    
    
