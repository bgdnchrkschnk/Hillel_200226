list_of_numbers: list = [1, 2, 3, 4, 5]
list_of_random_data: list = [1, "Bohdan", True, 1.23, [1,2,3], (), None]

empty_list = []
empty_list_2 = list()


first_element = list_of_numbers[0]
second_element = list_of_numbers[1]
last_element = list_of_numbers[-1]

print(first_element)
print(second_element)
print(last_element)

list_of_random_data[0] = "First element"
print(list_of_random_data)


# change positions in list elements
list_of_random_data[1], list_of_random_data[3] = list_of_random_data[3], list_of_random_data[1]

print(list_of_random_data)

"""
a=1
b=2
a,b = b,a
"""

number_three: int = list_of_numbers[2] # -> 3 (int)
list_with_number_three: list = list_of_numbers[2:3] # -> [3] (list)

# converting to list
welcome_message: str = "Welcome to Python"
list_of_letters: list = list(welcome_message)

tuple_numbers: tuple = (1,2,3,4,5)
list_of_numbers: list = list(tuple_numbers)

my_dict: dict = {"name": "Bohdan", "age": 29}
my_dict_items = my_dict.items() # -> dict_items([('name', 'Bohdan'), ('age', 29)])
list_of_dict_items: list[tuple] = list(my_dict_items)
list_of_dict_keys: list[str] = list(my_dict)

print(list_of_dict_items)
print(list_of_dict_keys)

# count, index
list_of_numbers_new: list = [1,2,3,4,5,6,4,3, None, None, (1,), (1,)]

count_of_None = list_of_numbers_new.count(None)
count_of_1 = list_of_numbers_new.count(1)
print("Number of None: ", count_of_None)
print("Number of 1: ", count_of_1)

# ----------------

index_of_first_1 = list_of_numbers_new.index(1)
# index_of_second_1 = list_of_numbers_new.index(1, index_of_first_1 + 1) # Value Error - No element found
print("Index of first 1: ", index_of_first_1)

for _ in range(10):
    print(_)