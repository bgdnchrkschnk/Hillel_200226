from pprint import pprint


class Car:
    wheels = 4
    engine = 1

    def __init__(self, model_param, v_engine_param, color_param, date_of_purchase_param, tank_param=30): # magic method (constructor init) (Dunderscore)
        self.model = model_param
        self.v_engine = v_engine_param
        self.color = color_param
        self.date_of_purchase = date_of_purchase_param
        self.tank = tank_param
        self.usage_gas = 0.5

    def drive_to(self, destination, km):
        to_use_gas: float = km * self.usage_gas # рахуємо скільки пального витратимо

        if to_use_gas > self.tank: # перевірка в бакі
            print("Not enough gas")
            return
        else:
            print(f"Driving to {destination}. Estimated gas usage: {to_use_gas} liters")
            self.tank: float = self.tank - to_use_gas
            print(f"Tank remain: {self.tank} liters")


# toyota_camry = Car(model="Camry", v_engine=1.6, color="red", date_of_purchase="2022-01-01")
porshe_911 = Car("911", 1.4, "black", "2021-01-01") # init


# porshe_911.drive_to(destination="Berlin")
#
# print(
#     dir(toyota_camry)
# )
# print(
#     dir(porshe_911)
# )
#
# print(toyota_camry.wheels)
# print(porshe_911.wheels)
#
#
# toyota_camry.drive_to(destination="London")
# porshe_911.drive_to(destination="Paris")
#
# Car.drive_to(toyota_camry, destination="Berlin")
# toyota_camry.drive_to(destination="Berlin")


cadillac_escalade: Car = Car("Escalade", 1.6, "white", "2020-01-01")

print(cadillac_escalade.tank)
cadillac_escalade.drive_to(destination="Kyiv", km=40)






