from app.models.user import User
from app.models.car import Car
from app.models.transaction import Transaction

class HomeAdminController:

    def __init__(self, username):
        self.user = User(username)
        self.transaction = Transaction()

    def showAllTransaction(self):
        return self.transaction.showAll()
    
    def showTableData(self):
        data = []
        alltransaction = self.showAllTransaction()
        for i in alltransaction:
            dict_data = {}
            for key, value in i.items():
                if key == "_id":
                    continue
                elif key == "id_car":
                    id_car = value
                    c = Car(id_car)
                    dict_data['car_brand'] = c.getBrand()
                    dict_data['car_model'] = c.getModel()
                    dict_data['license_plate'] = c.getLicensePlate()
                else:
                    dict_data[key] = value
            data.append(dict_data)
        return data

    def getNameUser(self):
        return self.user.getName()
    
    def deleteTransaction(self, no):
        indeks = int(no)-1
        alltransaction = self.showAllTransaction()
        transaction = alltransaction[indeks]
        id_transaction = transaction['_id']
        t = Transaction(id_transaction)
        t.deleteThisTransaction()

    