from work_with_files import fake
from random import choice, choices, randint
import json

# "+34" +""".join(choices(["0", "1", "2", "3", "4"], k=8))

person_dict = {
    "name": fake.name(),
    "email": fake.email(),
    "age": randint(18, 65),
    "phone": fake.phone_number(),
    "address": fake.street_address(),
    "is_married": choice([True, False]),
    "friends": [fake.name() for i in range(randint(1, 10))]
}

# --------------------- .dump() -> python dict to json file

with open("person.json", "w") as json_file:
    json.dump(person_dict, json_file, indent=4)


# ---------------------- .dumps() -> python dict to json string

person_dict_json: str = json.dumps(person_dict, indent=4)
print(person_dict_json)

# ---------------------- .load() -> read json file and convert to python dict

with open("person.json", "r") as json_file:
    person_dict_from_file: dict = json.load(json_file)
    # print(person_dict_from_file["friends"])

# ---------------------- .loads() -> read json string and convert to python dict

person_dict_json_converted_to_dict: dict = json.loads(person_dict_json)
# print(person_dict_json_converted_to_dict["friends"])


# ---------------------------------------------


invalid_json = '{"name": "Ivan" "age": 29, "friends": ["John", "Mary", "Jane"]}'

try:
    json.loads(invalid_json)
except json.JSONDecodeError as e:
    print("json string is invalid")



with open("invalid.json", "r") as json_file:
    try:
        json.load(json_file)
    except json.JSONDecodeError as e:
        print("json file is invalid")


