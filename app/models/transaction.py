import pymongo
from bson.objectid import ObjectId

class Transaction:
    def __init__(self, id=None):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["rental"]
        self.col_transactions = db["transactions"]
        if id:
            self.id = ObjectId(id)
    
    def showAll(self):
        arr = []
        for x in self.col_transactions.find():
            arr.append(x)
        return arr

    def getData(self):
        return self.col_transactions.find_one({"_id":self.id})

    def add(self, id_car, duration, buyer_name, buyer_address, buyer_phone, buyer_idcard, price_total):
        dict_transaction = {"id_car":id_car, "duration":duration, "buyer_name":buyer_name, "buyer_address":buyer_address, "buyer_phone":buyer_phone, "buyer_idcard":buyer_idcard, "price_total":price_total}
        return self.col_transactions.insert_one(dict_transaction)
    
    def deleteThisTransaction(self):
        query = { "_id": self.id }
        return self.col_users.delete_one(query)

    def getId(self):
        return self.id
    
    def getBuyerName(self):
        get = self.col_transactions.find_one({"_id":self.id}, {"buyer_name" : 1})
        if get == None:
            return None
        return get['buyer_name']
    
    def setBuyerName(self, buyer_name):
        new = { "$set": { "buyer_name": buyer_name } }
        return self.col_transactions.update_one({"_id":self.id}, new)
    
    def getDuration(self):
        get = self.col_transactions.find_one({"_id":self.id}, {"duration" : 1})
        if get == None:
            return None
        return get['duration']
    
    def setDuration(self, duration):
        new = { "$set": { "duration": duration } }
        return self.col_transactions.update_one({"_id":self.id}, new)
    
    def getBuyerAddress(self):
        get = self.col_transactions.find_one({"_id":self.id}, {"buyer_address" : 1})
        if get == None:
            return None
        return get['buyer_address']
    
    def setBuyerAddress(self, buyer_address):
        new = { "$set": { "buyer_address": buyer_address } }
        return self.col_transactions.update_one({"_id":self.id}, new)
    
    def getBuyerPhone(self):
        get = self.col_transactions.find_one({"_id":self.id}, {"buyer_phone" : 1})
        if get == None:
            return None
        return get['buyer_phone']

    def setBuyerPhone(self, buyer_phone):
        new = { "$set": { "buyer_phone": buyer_phone } }
        return self.col_transactions.update_one({"_id":self.id}, new)
    
    def getBuyerIdCard(self):
        get = self.col_transactions.find_one({"_id":self.id}, {"buyer_idcard" : 1})
        if get == None:
            return None
        return get['buyer_idcard']

    def setBuyerIdCard(self, buyer_idcard):
        new = { "$set": { "buyer_idcard": buyer_idcard } }
        return self.col_transactions.update_one({"_id":self.id}, new)
    
    def getPriceTotal(self):
        get = self.col_transactions.find_one({"_id":self.id}, {"price_total" : 1})
        if get == None:
            return None
        return get['price_total']

    def setPriceTotal(self, price_total):
        new = { "$set": { "price_total": price_total } }
        return self.col_transactions.update_one({"_id":self.id}, new)

