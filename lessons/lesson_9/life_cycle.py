class User:

    def __init__(self, username, age, sex): # init -> initialization
        self.username = username
        self.age = age
        self.sex = sex

    def __del__(self):
        print(f"Deleting {self.username}")
        ...

    def say_hello(self):
        print("Hello")

# LIFECYCLE

# CONSTRUCTOR (initialization)
volodya = User("Volodymyr", 20, "male")
mykhailo = User("Mykhailo", 20, "male")

# Utilization of the object
print(volodya.username)
print(volodya.age)
print(volodya.sex)
volodya.hobbies = ["programming"]
print(volodya.hobbies)
volodya.say_hello()


# DESTRUCTOR (destruction)

del volodya
volodya.say_hello()