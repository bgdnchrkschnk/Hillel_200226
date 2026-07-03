# tuple declare (+ whout ())

# tuple 1 element
# convert data to tuple (str, list, dict...)
# tuple index, slice (not index assign editing)
my_tuple = (1,2,"three",3.14,True, 3.14)
three_lst_letter = my_tuple[2][-1]


# tuple count vs str count
# tuple index vs str index(find)   -> tuple.index(value, start=0, stop=len(tuple))
# tuple is immutable comparing to list -> t[0] = 10 <- пробуємо змінити елемент
# CONST vars

# list declare, index, slice (diff types data inside)
# convert to list from tuple, str, dict
# list count, index

# list modification (append  <- show with ids
# modify inner data
list_v1 = ["Bohdan", 29, 36.6, ["Nikita", "Denys"], True, (1,2,3), None]
list_v1[3].append("Daniel")

tuple_v1 = ("Bohdan", 29, 36.6, ["Nikita", "Denys"], True, (1,2,3), None)
tuple_v1[3].append("Daniel") # можна тому що id не змінюється
print(tuple_v1)




list_1 = [1,2,3]
list_2 = ["one", "two", "three"]
print(id(list_1), list_1)
print(id(list_2), list_2)
tuple_of_lists = list_1, list_2
print(id(tuple_of_lists), tuple_of_lists)
list_1.append(4)
print(id(list_1), list_1)
print(id(tuple_of_lists), tuple_of_lists)

# list copies
my_numbers = [1,2,3]
my_numbers_copy = my_numbers # <- invalid
# my_numbers_copy = my_numbers.copy()
# my_numbers_copy = my_numbers[:]
# my_numbers_copy = list(my_numbers)
my_numbers_copy.append(4)
print(my_numbers)
print(my_numbers_copy)

# copy vs deepcopy

import copy
original = [[1, 2], [3, 4]]

not_deep_copy = copy.copy(original)     # поверхнева копія
deep = copy.deepcopy(original)    # глибока копія

# змінюємо вкладені в оригінальному списку
original[0][0] = 99

print("Original:", original)
print("not deep copy:", not_deep_copy)
print("Deep:", deep)

# append vs extend vs + concatenate vs insert
l1 = [1,2,3]
l2 = [4,5,6]
l1 + l2 # нічого не буде

# pop, remove, clear
# range
list_of_numbers = list(range(10))

for i in range(5):
    print(i)
# Вивід: 0 1 2 3 4
# sort vs sorted
words = ["banana", "Apple", "cherry", "apple", "Banana"]
print(sorted(words))

# sort key
"""відсортувати по довжині імені

# len(k)  - довжина к

# lambda x: len(x)
# lambda  - кключове слово
# lambda x: - для кокжного елемента в списку, це елемент ми записуємо в змінну х\
# lambda x: len(x), len(x) - визначає довжину x, тобто довжину ккожного слова
# на виході у нас список із довжин слів
# ['Den', 'Alex', 'Ivan', 'Alice', '1', '%$%'] => [3, 4, 5, 6, 1, 3]
# ми сортуємо [3, 4, 5, 6, 1, 3]"""

my_list = ['Den', 'Alex', 'Ivan', 'Alice', '1', '%$%']

my_list.sort(key=lambda x: len(x)) # від найкоротшого до найдовшого слова
print(my_list)
# my_list.sort(key=lambda x: len(x), reverse=True) # від найдовшого до найкоротшого слова
# print(my_list)



#---------------------
# відсортувати за оцінкою
tuple_of_scores = [("Roman", 100), ("Ivan", 90), ("Alex", 80)]

tuple_of_scores.sort(key=lambda x: x[1], reverse=True)
print(tuple_of_scores)


# list comprehension

welcome_str = "Hello, world!"
list_ = []

for letter in welcome_str:
    if letter != " ":
        list_.append(letter)

# --------------------
user_data = [
    (1, 90),
    (2, 55),
    (10, 94),
    (11, 94),
    (13, None),
    (6, 77)
]

# кількість юзерів зі скором більше 60

prepare_count_of_users = [1 for k in user_data if k[1] is None and k[1] > 60 ]
count_of_users = sum(prepare_count_of_users)
print(prepare_count_of_users)
print(count_of_users)



