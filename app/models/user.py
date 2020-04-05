import pymongo

class User:

    """ Jika bikin object tanpa username, maka digunakan untuk menambah data atau menampilkan
    semua data, jika ada username untuk mendapatkan informasi user"""
    def __init__(self, username=None):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["rental"]
        self.col_users = db["users"]
        if username:
            self.username = username

    def getData(self):
        return self.col_users.find_one({"username":self.username})
    
    def add(self, name, address, email, username, password, phone, role):
        dict_user = {"name":name, "address":address, "email":email, "phone":phone, "username":username, "password":password, "role":role}
        return self.col_users.insert_one(dict_user)
    
    def showAll(self):
        arr = []
        for x in self.col_users.find():
            arr.append(x)
        return arr
    
    def deleteThisUser(self):
        query = { "username": self.username }
        return self.col_users.delete_one(query)
        
    def getName(self):
        get = self.col_users.find_one({"username":self.username}, {"name" : 1})
        if get == None:
            return None
        return get['name']
    
    def setName(self, name):
        new = { "$set": { "name": name } }
        return self.col_users.update_one({"username":self.username}, new)

    def getUsername(self):
        return self.username
    
    def setUsername(self, username):
        new = { "$set": { "username": username } }
        return self.col_users.update_one({"username":self.username}, new)
    
    def getAddress(self):
        get = self.col_users.find_one({"username":self.username}, {"address" : 1})
        if get == None:
            return None
        return get['address']
    
    def setAddress(self, address):
        new = { "$set": { "address": address } }
        return self.col_users.update_one({"username":self.username}, new)
    
    def getEmail(self):
        get = self.col_users.find_one({"username":self.username}, {"email" : 1})
        if get == None:
            return None
        return get['email']

    def setEmail(self, email):
        new = { "$set": { "email": email } }
        return self.col_users.update_one({"username":self.username}, new)
    
    def getPassword(self):
        get = self.col_users.find_one({"username":self.username}, {"password" : 1})
        if get == None:
            return None
        return get['password']

    def setPassword(self, password):
        new = { "$set": { "password": password } }
        return self.col_users.update_one({"username":self.username}, new)
    
    def getRole(self):
        get = self.col_users.find_one({"username":self.username}, {"role" : 1})
        if get == None:
            return None
        return get['role']
        



