from app.models.user import User
from app.models.car import Car
from app.models.transaction import Transaction

class HomeUserController:
    def __init__(self, username):
        self.user = User(username)
        self.car = Car()
        self.transaction = Transaction()
    
    def getNameUser(self):
        return self.user.getName()
    
    def addTransaction(self, id_car, rent_date, duration, buyer_name, buyer_address, buyer_phone, buyer_idcard, buyer_birth, price_total):
        return self.transaction.add(id_car, rent_date, duration, buyer_name, buyer_address, buyer_phone, buyer_idcard, buyer_birth, price_total)

    def showAllCar(self):
        return self.car.showAll()

    def showAllPlatCar(self):
        allplat = []
        allcar = self.showAllCar()
        for i in allcar:
            allplat.append({i['license_plate']:i['_id']})
        return allplat
    
    def getBrandCar(self, id):
        c = Car(id)
        return c.getBrand()
    
    def getModelCar(self, id):
        c = Car(id)
        return c.getModel()
    
    def getColorCar(self, id):
        c = Car(id)
        return c.getColor()
    
    def getPriceCar(self, id):
        c = Car(id)
        return c.getPrice()
    
    def getTotalPrice(self, id, duration):
        price = self.getPriceCar(id)
        return price*duration
    





