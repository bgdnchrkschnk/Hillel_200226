# INHERITENCE

class Animal:
    eyes = 2
    legs = 4

    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def move(self):
        if type(self) == Cat:
            print("Cat Moving")
        elif type(self) == Dog:
            print("Dog Moving")
        elif type(self) == MiniDog:
            print("Mini Dog Moving")
        else:
            print("Animal Moving")


class Dog(Animal):

    def __init__(self, name, date_of_birth, breed, character):
        super().__init__(name, date_of_birth)
        self.breed = breed
        self.character = character

    # def move(self):
    #     print("Dog is moving")


class MiniDog(Dog):
    def __init__(self, name, date_of_birth, breed, character, mini_dog_size):
        super().__init__(name, date_of_birth, breed, character)
        self.mini_dog_size = mini_dog_size

    # def move(self):
    #     print("Mini Dog is moving")

class Cat(Animal):

    def __init__(self, name, date_of_birth):
        super().__init__(name, date_of_birth)

    # def move(self):
    #     print("Cat is moving")


dog_1 = Dog("Max", "2022-01-01", "Labrador", "Friendly")
mini_dog_1 = MiniDog("Max", "2022-01-01", "Labrador", "Friendly", "Small")
cat_1 = Cat("Max", "2022-01-01")


# POLIMORPHYSM

my_animals = [dog_1, cat_1, mini_dog_1]

# for animal in my_animals:
#     animal.move()




# Incapsulation


class BankAccount:
    def __init__(self, name, type_card="classic"):
        self.name = name # public
        self.__create_start_balance() # private
        self._type_card = type_card # protected


    def add_balance(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def __create_start_balance(self): # private
        self.__balance = 0




bgdn = BankAccount("Bohdan")
bgdn._type_card = "gold"

bgdn.add_balance(100)
print(
    bgdn.get_balance()
)
bgdn.__create_start_balance()






