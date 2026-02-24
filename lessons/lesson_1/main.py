print("my name is Bohdan")


my_name: str = 'Bohdan' # строчка
my_age: int = 25 # ціле число
my_temperature: float = 36.6 # число з плаваючою точкою
am_i_student: bool = True # правда або неправда
my_friends: list = ['Ivan', 'Oleg', 'Nikita'] # список з значень
my_parents: tuple = ("Mommy", "Daddy") # незмінний список
locations_i_ve_been: set = {"Ukraine", "Russia", "Poland"} # набір значень без індексації, без дублікатів
empty = None
my_biography: dict = {"name": my_name, "age": my_age, "friends": my_friends} # словник аналог JSON


print(
    29 == "29" # оператор порівняння
)
print(
    my_age == 25
)


# 1_my_parents
# my_friends_<3 = 63 # no symbols


# snake_case - для основних змінних
my_age_in_years = my_age * 365

# CONSTANT
MY_GENDER = "male"

# CamelCase
class PersonOfTheYear:
    pass


name_of_person = "Ivan"
name_of_person_copy = name_of_person # один айдішник

print(id(name_of_person))
print(id(name_of_person_copy))

name_of_person = "Oleg"
print(id(name_of_person))
print(id(name_of_person_copy))


test_string = "test_string"
test_string_2 = test_string + " copy"
print(id(test_string))
print(id(test_string_2))


# for i in range(10):
#   print(i)
# print("----")

first_number = 10.80
second_number = 20
sum_of_numbers = first_number + second_number
print(sum_of_numbers)


print(
    "20" + "100"
)

a = 5
b = 3

summ = a + b  # Додавання
diff = a - b  # Віднімання
mult = a * b  # Множення
divd = a / b  # Ділення
div_2 = a // b # Ділення без остатку

print(summ, diff, mult, divd, div_2, sep="\t", end="!!!")