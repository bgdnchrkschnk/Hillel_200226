

# АТРИБУТИ КЛАСУ (property, методи)
#




class Car: # CamelCase format    MyCarClassForDrive (camel case->class)    my_car_class_for_drive (snake_case->funcs)
    wheels = 4
    engine = 1

    @staticmethod
    def drive_to(destination):
        print(f"Driving to {destination}")

# Car.drive_to("London")
#drive_to
#wheels
#engine


# Instance(екземпляр) - це обʼєкт класу (конкретна створена машинка)
my_car: Car = Car() # instance of class
my_car_2: Car = Car()
my_car_3: Car = Car()

print(id(my_car))
print(id(my_car_2))


print(
    my_car.wheels,
    my_car.engine,
)

# Car.drive_to(destination="Paris")

my_car.drive_to(destination="London")



class SportsMan:
    ...


klitchko: SportsMan = SportsMan()

