from pprint import pp, pprint
from statistics import kde_random


# СТАТИЧНІ ФУНКЦІЇ

# функція повертає None, тобто нічого
def print_biography() -> None:
    name = "Donal Trump"
    age = 75
    print(f"My name is {name}. My age is {age}")


# print_biography() # call (виклик)

# функція повертає щось через return
def return_biography() -> str:
    ...
    ...
    ...
    ...
    ...
    name = "Donal Trump"
    age = 75
    return f"My name is {name}. My age is {age}"

result = return_biography()
# print(result)
# ---------------------------------------------------------------
# ДИНАМІЧНІ ФУНКЦІЇ

def print_biography_dynamic(name, age) -> None:
    biography = f"My name is {name}. My age is {age}"
    print(biography)

def return_biography_dynamic(name, age) -> str:
    biography = f"My name is {name}. My age is {age}"
    return biography

# print_biography_dynamic(name="Donal Trump", age=75)
print_biography_dynamic("Joe Biden", 82)
print_biography_dynamic(age=82, name="Joe Biden")

# print(
#     return_biography_dynamic("Jeff Bezos", 36)
# )


person_1: dict = {
    "name": "Donal Trump",
    "age": 75,
    "city": "Washington, D.C.",
}

person_2: dict = {
    "name": "Joe Biden",
    "age": 82,
    "city": "New York",
}


def describe_person(random_person_dict: dict, return_data: bool = True) -> str | None:
    name = random_person_dict.get("name")
    age = random_person_dict.get("age")
    city = random_person_dict.get("city")
    bio = f"Person {name} is {age} years old. He lives in {city}."
    if return_data:
        return bio
    print(bio)


describe_person(person_1, return_data=False)
biography_person_2 = describe_person(person_2)
# print(biography_person_2)


# ---------------------------------------
def average_result(*args):
    # args: tuple[...]
    print(args)
    average = sum(args)/len(args)
    for number in args:
        print(number)
    return average

# numbers = [1,2,3,4,5,6,7,8,9,10]
average = average_result(5, 0, -1, 29.8)
# ------------------------------

def all_str_concatenation(*args):
    tuple_of_str = args
    result = ":".join(tuple_of_str)
    print(result)


all_str_concatenation("Hello", "World", "!", "jkbsf", "nejfw")


# -------------------------------------------------------------------------

def print_biography_dynamic_v2(**kwargs):
    print(type(kwargs), kwargs) # kwargs - dict
    bio = ""
    for key, value in kwargs.items():
        bio += f"{key}: {value} "
    print(bio)



print_biography_dynamic_v2(name="Jeff", surname="Bezos", age=36, profession="CEO", favorite_color="red", is_married=True)
print_biography_dynamic_v2(name="Jordan", best_friend="Donald",experience=10)


# ---------------------------



def print_biography_dynamic_v2(name, age, **extra_info):
    bio = f"My name is {name}. My age is {age}. "

    if extra_info: # if
        extra_info_str = "\nExtra info:"
        for key, value in extra_info.items():
            extra_info_str += f"{key}: {value} "
        bio += extra_info_str


    print(bio)

print_biography_dynamic_v2("Bohdan", 29, profession="CEO", favorite_color="red", is_married=False)


# -------------------------------------------

def candidate_for_job(*skills, **candidate_info) -> None:
    candidate_cv = {
        "candidate_info": candidate_info,
        "skills": skills,
    }
    pprint(candidate_cv)

candidate_for_job("Python", "SQL", "API", "RESTful", "Selenium", z="z", name="Maxim", experience=10, salary=10000, city="Kyiv")

