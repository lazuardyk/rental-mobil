import pymongo

class Migrate:
    def __init__(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["rental"]
        col_users = db["users"]
        col_users.create_index("email", unique=True)
        col_users.create_index("username", unique=True)

        dict_user = [
            {"name":"Lazuardy User", "address":"Waru Doyong 123", "email": "user@user.com", "phone":"081395863285", "username":"user", "password":"user", "role":"user"},
            {"name":"Lazuardy Admin", "address":"Waru Doyong 123", "email": "admin@admin.com", "phone":"081395863285", "username":"admin", "password":"admin", "role":"admin"}
        ]
        col_users.insert_many(dict_user)

        col_cars = db["cars"]
        dict_cars = [
            {"brand":"Toyota", "model":"Avanza", "color":"Merah", "license_plate":"B 374 K", "price_per_day":100000, "production_year": "2012"},
            {"brand":"Daihatsu", "model":"Xenia", "color":"Silver", "license_plate":"B 373 K", "price_per_day":200000, "production_year": "2011"}
        ]
        inserted_cars = col_cars.insert_many(dict_cars)
        idinserted_cars = inserted_cars.inserted_ids

        col_transactions = db["transactions"]

        dict_transactions = [
            {"id_car": idinserted_cars[0], "rent_date":"15-04-2020", "duration":"2", "buyer_name": "Laz buyer", "buyer_address":"Jl Daksin 123", "buyer_phone": "081395863941", "buyer_idcard":"3306124403910302", "buyer_birth":"10-10-2000", "price_total": 200000}
        ]

        col_transactions.insert_many(dict_transactions)

        
        # print(client.list_database_names())
        # print(db.list_collection_names())

if __name__ == "__main__":
    m = Migrate()