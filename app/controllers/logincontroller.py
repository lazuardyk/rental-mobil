from app.models.user import User

class LoginController:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def checkLogin(self):
        u = User(self.username)
        password = u.getPassword()
        if self.password == password:
            return True
        return False
    
    def checkRole(self):
        u = User(self.username)
        return u.getRole()