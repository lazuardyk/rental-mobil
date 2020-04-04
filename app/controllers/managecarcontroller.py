from app.models.car import Car

class ManageCarController:

    def __init__(self):
        self.car = Car()
    
    def showAllCar(self):
        return self.car.showAll()
    
    def addCar(self, brand, model, color, license_plate, price_per_day, production_year):
        return self.car.add(brand, model, color, license_plate, price_per_day, production_year)
    
    #todo
    def deleteCar(self, no_polisi):
        pass