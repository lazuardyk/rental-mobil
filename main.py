from app.main import Main
from app.controllers.homeusercontroller import HomeUserController
from app.controllers.managecarcontroller import ManageCarController

if __name__ == "__main__":
    m = Main()
    m.run()
    # h = HomeUserController("user")
    # h.showAllPlatCar()
    # m = ManageCarController()
    # print(m.showAllCar())