def divide(a, b):
    return a / b

data = [(10,5), (2, -1), (0, 5), (2, 0), (10, 10), (10, 2), (4, None)]


# for a, b in data:
#     try:
#         print(divide(a, b))
#     except ZeroDivisionError:
#         print(f"It was not possible to divide {a} by {b}")
#     except TypeError:
#         print(f"One of the arguments is not a number: {a} or {b}")
#     finally:
#         print("Finally printed in console...")




# try except else finally

# try:
#     print(divide(10, "jwnfejknk"))
# except (ZeroDivisionError, TypeError):
#     print("Division by zero is not allowed!")
# finally:
#     print("Finally printed in console...")

#
# try:
#     postgres_connector = sqlpostgres.connect(**config)
#     postgres_connector.insert("INSERT")
# except Exception:
#     print("Connection error occurred.")
# finally:
#     postgres_connector.close()

def is_adult(age: int):
    if age >= 18:
        return "Adult"
    elif age <= 0:
        raise ValueError(f"Age cannot be {age}")
    else:
        return "Child"



# list_of_ages = [12, 18, 20, 25, 30, 1, 99, 0, -6, "66"]
# for age in list_of_ages:
#     try:
#         print(age, is_adult(age))
#     except Exception as e:
#         print(f"Something went wrong", e)
#     finally:
#         print("Process finished")
#

list_of_ages = [12, 18, 20, 25, 30, 1, 99]

try:
    for age in list_of_ages:
        print(age, is_adult(age))
except Exception as e:
    print(f"Something went wrong", e)
else: # тільки коли виконалось без помилок try_block
    print("All data processed successfully")
finally: # завжди
    print("Process finished")








