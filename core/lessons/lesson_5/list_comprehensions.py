# list comprehension
from platform import python_version
from traceback import print_exc

numbers_range = range(1, 11)
list_of_numbers_range = list(numbers_range)

print(list_of_numbers_range)

new_final_filtered_list = []

for number in list_of_numbers_range:
    if number % 2 == 0:
        new_final_filtered_list.append(number)

print(new_final_filtered_list)

# ----------

new_final_filtered_list_2: list = [number for number in range(1,11) if number % 2 == 0]
print(new_final_filtered_list_2)

# -------------

users_list = [
    {
        "name": "Bohdan",
        "age": 29
    },
    {
        "name": "Oleg",
        "age": 18
    },
    {
        "name": "Mykola",
        "age": 14
    },
    {
        "name": "Vasya",
    }
]

to_enter_available: list = [person for person in users_list if person.get("age") is not None if person.get("age") >= 18]
print(to_enter_available)
