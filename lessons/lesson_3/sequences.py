from lessons.lesson_3.operations import list_of_numbers

user_id = 123456789
actual_status_code = 401
json_response = {"error": "Unauthorized",
                 "msg": "User is not authorized",
                 "status_code": actual_status_code,
                 "user_id": user_id,
                }

log_payment: str = f'I\'m Making payment operation for user {user_id}. \nExpected status_code: 200 \nActual status_code: {actual_status_code} \nResponse_body: {json_response}'
my_biography: dict = {
    "name": "bohdan",
    "age": 29,
    "friends": ["Oleg", "Ivan"]
}


print(len(log_payment))
print(len(my_biography))


# ---------------------------------
list_of_numbers: list = [1,2,3,4,5,6,7,8,9,10]
tuple_of_numbers: tuple = (1,2,3,4,5,6,7,8,9,10)


element_1 = log_payment[0]
element_2 = log_payment[1]
print(element_1)
print(element_2)

last_element = tuple_of_numbers[-1]


len_of_tuple = len(tuple_of_numbers)

print("len of tuple", len_of_tuple)
last_element = tuple_of_numbers[len_of_tuple - 1]
print(last_element)


# --------------------------------
slice_from_1_to_5 = list_of_numbers[0:5] # -> list
slice_from_3_to_7 = list_of_numbers[2:7]
slice_from_1_to_5 = list_of_numbers[:5] # -> [0:5]
slice_from_5_to_end = list_of_numbers[4:] # -> [4:-1]
slice_ = list_of_numbers[-6:-3]
print(slice_from_1_to_5)
print(slice_from_3_to_7)
print(slice_from_1_to_5)
print(slice_from_5_to_end)
print(slice_)

# ----------------------------------
# [start:end:step]

every_second_element = list_of_numbers[::2]

print(every_second_element)

reverse_list = list_of_numbers[::-1]
print(reverse_list)

reversed_every_second_element = list_of_numbers[::-2]
print(reversed_every_second_element)


reversed_from_half = list_of_numbers[-3:-9:-1]
print(reversed_from_half)


for i in list_of_numbers[::-1]:
    print(i)


print(10/0)