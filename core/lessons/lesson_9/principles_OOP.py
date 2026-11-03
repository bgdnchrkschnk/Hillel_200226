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
"""
**Поліморфізм** — це можливість використовувати **одне й те саме ім'я методу (або інтерфейс)** для об'єктів різних типів, отримуючи **різну поведінку** залежно від конкретного класу об'єкта.
"""

my_animals = [dog_1, cat_1, mini_dog_1]

# for animal in my_animals:
#     animal.move()

# Одинаковий виклик .move() для різних об'єктів
animals = [Cat(), Dog(), MiniDog(), Animal()]

for animal in animals:
    animal.move()

# Функції все одно, який тип об'єкта сюди передали —
# головне, що у нього є метод .move()
def make_it_move(obj):
    obj.move()

make_it_move(Cat())      # Cat Moving
make_it_move(Dog())      # Dog Moving
make_it_move(MiniDog())  # Mini Dog Moving
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


class BankAccount:
    def __init__(self, owner, account_type, balance, pin):
        # Public: відкрита інформація
        self.owner = owner

        # Protected (_): внутрішня логіка, доступна класу та його спадкоємцям
        self._account_type = account_type

        # Private (__): захищено від випадкового перезапису (Name Mangling)
        self.__balance = balance
        self.__pin = pin

        # Публічний метод для безпечної роботи з приватними даними

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Поповнено на {amount}. Поточний баланс: {self.__balance}")

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("Помилка: Невірний PIN-код!")
            return
        if amount > self.__balance:
            print("Помилка: Недостатньо коштів!")
            return

        self.__balance -= amount
        print(f"Знято {amount}. Залишок: {self.__balance}")


