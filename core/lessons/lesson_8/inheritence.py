class Animal:
    eyes = 2
    tail = 1
    head = 1
    alive = True

    def move(self):
        print("Moving")

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

    def make_sound(self):
        print("Making Sound!")

    # def print_self(self):
    #     print(self)
    #

class Dog(Animal):
    ...

class Cat(Animal):

    def make_sound(self):
        print("Meow!")

    def scratch(self):
        print("Scratching")

dog_1 = Dog() # instance of class
dog_2 = Dog()

cat_1 = Cat()
cat_2 = Cat()


# При наслідування клас наслідник отримує всі характеристики та поведінку від батьківського

dog_1.make_sound()
cat_1.make_sound()
cat_1.scratch()





