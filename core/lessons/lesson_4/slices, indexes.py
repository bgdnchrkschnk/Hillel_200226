welcome_message = "Welcome to AQA Python course!"


# indexes
first_letter = welcome_message[0]
last_letter = welcome_message[-1]
last_second_letter = welcome_message[-2]

# slices
course_name = welcome_message[10:21]
print(course_name)


# [start:end:step]


every_second_letter = welcome_message[::2]
reversed_message = welcome_message[::-1]
print(every_second_letter)
print(reversed_message)