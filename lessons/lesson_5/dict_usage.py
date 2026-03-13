my_bio = {
    "name": "Mykola",
    "age": 29,
    "job": "teacher"
} # # only immutable data in keys, value - all data


name = my_bio["name"]
empty_list = []
# my_bio[empty_list] = 33
my_bio["friends"] = empty_list

print(my_bio)


my_bio_extention = {
    "Favourite song": "The Weeknd - Never Gonna Give You Up",
    "Year of birth": 1996
}

# update

my_bio.update(my_bio_extention)
print(my_bio)


# -------------------------------- [key] vs .get()

job = my_bio["job"]
job_v2 = my_bio.get("job")

print(job)
print(job_v2)

# job = my_bio["car_model"]
car_model: str | None = my_bio.get("car_model", "No car data")

print(car_model)


empty_dict = {}
empty_dict_v2 = dict()


# -------------------

my_dict = dict(name="Mykola", age=29, job="teacher")
print(type(my_dict), my_dict)

# ---------------------------------------

print(my_bio)

for key in my_bio:
    print(key, my_bio[key])


for value in my_bio.values():
    print(value)

for key, value in my_bio.items(): # (key, value)
    print(key, value)

string = " hiuhiuehiuhwfhjkn  jkbeni urfghur egoiuhiuherkjf hujefwhu "
dict_of_letters_count = {}

for letter in string:
    if letter.isspace() is False: # isspace = True якщо це пробіл
        if not letter in dict_of_letters_count.keys():
            dict_of_letters_count[letter] = 1
        else:
            dict_of_letters_count[letter] += 1

print(dict_of_letters_count)

