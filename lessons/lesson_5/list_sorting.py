from email.contentmanager import raw_data_manager

random_numbers = [-5, 0, 15, 80.7, -160, 13]
print(id(random_numbers), random_numbers)

# # .sort() - доступний у всіх списків (list)
#
# random_numbers.sort() #
#
# print(id(random_numbers), random_numbers)
# random_numbers.sort(reverse=True)
# print(id(random_numbers), random_numbers)


# sorted() - глобальна функція для сортування колекцій

sorted_numbers = sorted(random_numbers)
sorted_numbers_reversed = sorted(random_numbers, reverse=True)

# print(id(sorted_numbers), sorted_numbers)
# print(id(sorted_numbers_reversed), sorted_numbers_reversed)
# print(id(random_numbers), random_numbers)


list_of_names = ["Ivan", "Olegjkjkescrrg", "Mykola", "Vasya", "Kol", "Andriy", "Artem"]
sorted_names = sorted(list_of_names)
print(sorted_names)

sorted_by_length = sorted(list_of_names, key=len, reverse=True) # [len("Ivan"), len("Olegjkjkescrrg"), len("Mykola"), len("Vasya"), len("Kol"), len("Andriy"), len("Artem")]
print(sorted_by_length)


list_of_persons: list[dict] = [
    {"name": "Ivan", "age": 29},
    {"name": "Oleg", "age": 29},
    {"name": "Mykola", "age": 45},
    {"name": "Vasya", "age": 29},
    {"name": "Kol", "age": 10},
    {"name": "Andriy", "age": 30},
    {"name": "Artem", "age": 44},
]
filtered_by_20_: list[dict] = [person_dict for person_dict in list_of_persons if person_dict['age'] > 20]

print(filtered_by_20_)

sorted_by_age = sorted(filtered_by_20_, key=lambda person_dict: (person_dict["age"], person_dict["name"]))
print(sorted_by_age)


all_in_one = sorted([person_dict for person_dict in list_of_persons if person_dict['age'] > 20], key=lambda person_dict: person_dict["age"])
print(all_in_one)

#
# def sort_by_age_and_name(person_dict: dict) -> tuple:
#     return (person_dict["age"], person_dict["name"])


