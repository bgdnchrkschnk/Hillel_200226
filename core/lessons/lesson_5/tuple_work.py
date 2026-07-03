my_tuple: tuple = (1,2,3)
my_tuple_v2: tuple = 1,2,3

my_data: tuple = ("Bohdan", 29, 36.6, ["Nikita", "Denys"], True, (1,2,3), None, {"name": "Bohdan"})

first_element = my_data[0]
last_element = my_data[-1]
print(first_element)
print(last_element)

name: str = my_data[0]
last_name = name[-1]

age: int = my_data[1]

print(last_name)

# tuple vs list (tuple is immutable)
my_data: tuple = ("Bohdan", 29, 36.6, ["Nikita", "Denys"])
my_data_list = ["Bohdan", 29, 36.6, ["Nikita", "Denys"]]

# my_data[0] = "Mykola"
my_data_list[0] = "Mykola"
print(my_data_list)


# tuple with one element

my_numbers: tuple = ("15",)

print(type(my_numbers), my_numbers)

# slices

numbers: tuple = (1,2,3,4,5,6,7,8)

from_2_to_5: list = numbers[1:5]

every_second_element = numbers[::2] # [start:end:step]
print(from_2_to_5)
print(every_second_element)


# ------------------------
# str to tuple
welcome_message: str = "Hello, my name is Bohdan"
welcome_message_tuple = tuple(welcome_message)
print(welcome_message_tuple)
# list to tuple
list_: list = [1,2,3,4,5]
tuple_: tuple = tuple(list_)
print(tuple_)
# dict to tuple

dict_: dict = {
    "name": "Bohdan",
    "age": 29
}
dict_items = dict_.items()
tuple_of_items: tuple = tuple(dict_items)
print(tuple_of_items)

# tuple_from_dict: tuple = tuple()
# print(tuple_from_dict)

# count, index
numbers: tuple = ("one", "two", "three", "four", "five", "two")
string = "My name is Bohdanaaaa"

count_of_one = numbers.count("one")
count_of_two = numbers.count("two")

count_of_a_in_string = string.count("a")


print(count_of_one)
print(count_of_two)
print(count_of_a_in_string)
# ----------------
# tuple.index() ~ str.find()
index_of_two: int = numbers.index("two", 0) # 1
index_of_two_second: int = numbers.index("two", index_of_two + 1) # [value, start_from]
print(index_of_two)
print(index_of_two_second)

# numbers[3] = "abhjef"

# CONST
SERVER_TIMEOUT: int = 5

# empty tuple
empty_tuple: tuple = ()
empty_tuple_2: tuple = tuple()

# якщо в незмінній колекції є змінна колекція - то її можна змінити
pre_inner_list = [1,2,3]
print(id(pre_inner_list), pre_inner_list)
my_random_tuple: tuple = (5632, 576.3674, None, pre_inner_list, True)

# my_random_tuple[-2].extend([4,5,6])
my_random_tuple[-2].append([4,5,6])
print(id(my_random_tuple[-2]), my_random_tuple[-2])

print(my_random_tuple)

inner_list = my_random_tuple[-2]
inner_inner_list = inner_list[-1]
print(inner_inner_list)


pre_inner_list.append(None)
print(id(pre_inner_list), pre_inner_list)
print(id(my_random_tuple[-2]), my_random_tuple[-2])


# -----------
from copy import deepcopy, copy

my_list = [1,2,3]
my_tuple = ("hef", None, my_list)
my_tuple_copy = deepcopy(my_tuple)

# deepcopy vs copy
# copy -> копіює обєкт з новим id але внутрішні елементи залишаються з тими же id
# deepcopy -> копіює обєкт з новим id але внутрішні елементи також копыюються  новими id

original = ([1, 2], [3, 4])

not_deep_copy = copy(original)
deep_copy = deepcopy(original)

original[0].append(3)

print(not_deep_copy)
print(deep_copy)





