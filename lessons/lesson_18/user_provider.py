from faker import Faker
from random import choice
fake = Faker()

def get_test_user():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "gender": choice(["male", "female"]),
        "status": "active"
    }