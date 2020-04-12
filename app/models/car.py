import pymongo
from bson.objectid import ObjectId

class Car:
    def __init__(self, id=None):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["rental"]
        self.col_cars = db["cars"]
        if id:
            self.id = ObjectId(id)
    
    def showAll(self):
        arr = []
        for x in self.col_cars.find():
            arr.append(x)
        return arr
    
    def getData(self):
        return self.col_cars.find_one({"_id":self.id})

    def add(self, brand, model, color, license_plate, price_per_day, production_year):
        dict_car = {"brand":brand, "model":model, "color":color, "license_plate":license_plate, "production_year": production_year, "price_per_day":price_per_day}
        return self.col_cars.insert_one(dict_car)
    
    def deleteThisCar(self):
        query = { "_id": self.id }
        return self.col_cars.delete_one(query)

    def getId(self):
        return self.id
    
    def getBrand(self):
        get = self.col_cars.find_one({"_id":self.id}, {"brand" : 1})
        if get == None:
            return None
        return get['brand']
    
    def setBrand(self, brand):
        new = { "$set": { "brand": brand } }
        return self.col_cars.update_one({"_id":self.id}, new)
    
    def getModel(self):
        get = self.col_cars.find_one({"_id":self.id}, {"model" : 1})
        if get == None:
            return None
        return get['model']
    
    def setModel(self, model):
        new = { "$set": { "model": model } }
        return self.col_cars.update_one({"_id":self.id}, new)

    def getColor(self):
        get = self.col_cars.find_one({"_id":self.id}, {"color" : 1})
        if get == None:
            return None
        return get['color']
    
    def setColor(self, color):
        new = { "$set": { "color": color } }
        return self.col_cars.update_one({"_id":self.id}, new)
    
    def getLicensePlate(self):
        get = self.col_cars.find_one({"_id":self.id}, {"license_plate" : 1})
        if get == None:
            return None
        return get['license_plate']
    
    def setLicensePlate(self, license_plate):
        new = { "$set": { "license_plate": license_plate } }
        return self.col_cars.update_one({"_id":self.id}, new)
    
    def getPrice(self):
        get = self.col_cars.find_one({"_id":self.id}, {"price_per_day" : 1})
        if get == None:
            return None
        return get['price_per_day']

    def setPrice(self, price_per_day):
        new = { "$set": { "price_per_day": price_per_day } }
        return self.col_cars.update_one({"_id":self.id}, new)

