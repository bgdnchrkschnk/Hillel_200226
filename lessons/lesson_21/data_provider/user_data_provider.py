from random import randint
from faker import Faker
from lessons.lesson_21.table_models.users_table import User
fake = Faker()


# def get_user():
#     user_dict = {
#         "name": fake.name(),
#         "age": randint(12, 69)
#     }
#     return User(**user_dict)


def get_user() -> User:
    return User(
        name=fake.name(),
        age=randint(12, 69)
    )



# oleg_dict = {"name": "Oleg", "age": 29}
#
# # user = User(name="Oleg", age=29)
# user = User(**oleg_dict)