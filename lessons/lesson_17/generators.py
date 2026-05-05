

# generator function (скінчений)
def get_name():
    yield "Oleg"
    yield "Mykola"
    yield "Ivan"


def get_name_2():
    for name in ["Oleg", "Mykola", "Ivan"]:
        yield name

generator = get_name() # generator object 1
generator_2 = get_name() # generator object 2

print(type(generator), id(generator))
print(type(generator_2), id(generator_2))

print(next(generator))
print(next(generator))
print(next(generator))

print(next(generator_2))





for el in generator_2:
    print(el)
def get_test_id():
    id_ = 1
    while True:
        yield f"TEST_ID:{id_}"
        id_ += 1


payment_test_id_generator = get_test_id() # generator object

print(
    next(payment_test_id_generator),
)

print(next(payment_test_id_generator))

# for el in payment_test_id_generator:
#     print(el)



# generator comprehension


list_to_1000000: list[int] = [i for i in range(100000000)] # list comprehension
set_to_1000000: set[int] = {i for i in range(1000000)} # set comprehension
dict_to_1000000: dict = {i: i for i in range(1000000)} # dict comprehension
generator_to_1000000 = (i for i in range(100000000)) # generator comprehension


print(type(generator_to_1000000), generator_to_1000000)


# Імпортуємо необхідні бібліотеки
import unittest
import requests

# Генератор для отримання даних з API
def api_data_generator():
    response = requests.get("https://api.example.com/data")
    for item in response.json():
        yield item


generator_object = api_data_generator()
generator_object_2 = api_data_generator()


# Клас для тестування відповіді API
class TestAPI(unittest.TestCase):
    # Тест для перевірки відповіді API
    def test_api_response(self):
        # Проходимо через кожен елемент, що генерується генератором
        for item in generator_object:
            # Перевіряємо, чи є отриманий елемент словником
            self.assertIsInstance(item, dict)
            # Перевіряємо наявність ключів "id" і "name"
            self.assertIn("id", item)
            self.assertIn("name", item)
            # Додаткові перевірки можна додати тут

# Запускаємо тестування, якщо файл запускається напряму
if __name__ == "__main__":
    unittest.main()

