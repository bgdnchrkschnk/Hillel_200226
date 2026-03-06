# append() - додати в кінець списку елемент
my_list: list = ["Bohdan", 29, 36.6, ["Nikita", "Denys"], True, (1,2,3), None]
print(id(my_list), my_list)
my_list.append("Daniel")
print(id(my_list), my_list)

# string analog (immutable)
string_1 = "Bohdan"
print(id(string_1), string_1)
string_2 = "Alice"
print(id(string_2), string_2)
string_1 = string_1 + string_2
print(id(string_1), string_1)

# extend - розширення іншим списком
my_list = [1,2,3]
print(id(my_list), my_list)
my_list_2 = [4,5,6]
print(id(my_list_2), my_list_2)
my_list.extend(my_list_2) # my_list.append(4) .append(5) .append(6)
print(id(my_list), my_list)


# COPY
my_numbers = [1,2,3]
my_numbers_copy = my_numbers

print(id(my_numbers), id(my_numbers_copy))
my_numbers_copy.append(5)
print(my_numbers, my_numbers_copy)

# ----------
my_numbers = [1,2,3]
my_numbers_copy = my_numbers.copy()
print(id(my_numbers), id(my_numbers_copy))

# ---------
my_numbers = [1,2,3]
my_numbers_copy = my_numbers[:]
print(id(my_numbers), id(my_numbers_copy))
# -------

my_numbers = [1,2,3]
my_numbers_copy = list(my_numbers)
print(id(my_numbers), id(my_numbers_copy))

# -----------

my_numbers = [1,2,3]
my_numbers_2 = [4,5,6]
my_numbers_3 = my_numbers + my_numbers_2 # extend analog
print(my_numbers_3)

my_numbers_list = [1,2,4,5,6]
my_numbers_list.insert(2, 3)
print(my_numbers_list)

# removing actions
# pop видаляє та повертає елемент по індексу
my_data = [1,2,3,4,5,6,7,8,9,10]

last_element = my_data.pop()
first_element = my_data.pop(0)
print(last_element, first_element)
print(my_data)


# ----------------
my_data = [1,2,"3",4,5,6,7,8,9,10, "3"]

my_data.remove("3")
print(my_data)

# ---------
# my_data.clear()

my_data = []
print(my_data)


