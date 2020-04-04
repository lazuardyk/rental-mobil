from app.models.car import Car

class ManageCarController:

    def __init__(self):
        self.car = Car()
    
    def showAllCar(self):
        return self.car.showAll()
    
    def addCar(self, brand, model, color, license_plate, price_per_day, production_year):
        return self.car.add(brand, model, color, license_plate, price_per_day, production_year)
    
    def getBrandCar(self, id):
        c = Car(id)
        return c.getBrand()
    
    def getModelCar(self, id):
        c = Car(id)
        return c.getModel()

    def deleteCar(self, id):
        c = Car(id)
        c.deleteThisCar()

    def showAllPlatCar(self):
        allplat = []
        allcar = self.showAllCar()
        for i in allcar:
            allplat.append({i['license_plate']:i['_id']})
        return allplat