def return_bio(name, age) -> str:
    return f"My name is {name}. My age is {age}"

lambda_return_bio = lambda name, age: f"My name is {name}. My age is {age}"

# print(
#     return_bio("Donal Trump", 75)
# )
# print(
#     lambda_return_bio("Donal Trump", 75)
# )
# ------------------------------------------------- filter(function, collection)
names = ["Donal Trump", "Joe", "Jeff Bezos", "Mark Zuckerberg"]

def is_len_name_more_than_3(name: str) -> bool:
    return len(name) > 3

# filtered_names = filter(lambda name: len(name) > 3, names) # [True, True, False, True]
filtered_names: filter = filter(is_len_name_more_than_3, names)
print(
    list(filtered_names)
)


# -------------------------------------- map(func, collection)
names = ["Donal Trump", "Joe", "Jeff Bezos", "Mark Zuckerberg"]


mapped_names: map = map(lambda name: name.upper(), names)
print(
    list(mapped_names)
)

# ----------------------------- zip()

list_of_names = ["Donal Trump", "Joe", "Jeff Bezos"]
list_of_ages = [75, 30, 45, 25]
list_of_cities = ["Washington, D.C.", "New York", "Los Angeles", "San Francisco"]

zipped_data = zip(list_of_names, list_of_ages, list_of_cities)
print(
    list(zipped_data)
)

list_of_more_than_35 = [True, False, True, False, True]

all_true = all(list_of_more_than_35)
print(all_true)


list_of_data = ["bhjef", "vdgwvh", 245, 0.1, True] # [bool("bhjef"), bool("vdgwvh"), bool(245), bool(0), bool(True) ]

all_true = all(list_of_data)
print(all_true)


# ----------------------------------------

list_of_data = [
    None, False, "", 1, 0.0
]

all_true = all(list_of_data)
any_true = any(list_of_data)

print(all_true)
print(any_true)


print(
    callable(all_true)
)


list_of_names = ["Donal Trump", "Joe", "Jeff Bezos"]

for index, name in enumerate(list_of_names):
    print(index, name)

res= enumerate(list_of_names)
print(list(res))


