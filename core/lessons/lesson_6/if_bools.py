
bool([])  # False
bool(dict())  # False
bool(tuple())  # False
bool(set())  # False
bool(False)  # False
bool(None)  # False
bool(0)  # False
bool(0.0)  # False
bool('')  # False

age = 1
list_of_data = [12]

if list_of_data: # bool(list_of_data)   len(list_of_data) != 0
    print('List is not empty')


if age: # bool(age)       age is not None
    print('Age is not None')






