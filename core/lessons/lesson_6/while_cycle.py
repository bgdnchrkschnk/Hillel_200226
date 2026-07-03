# string = "Hello"
#
# for letter in string:
#     print(letter)
import time
from random import randint

number = 0
limit = 10
while number < 10: # while condition:
    print(number)
    number += 1




# age = 13
#
# while age < 18:
#     print(f"You are only {age} ages. You are young")
#
#     time.sleep(1)
#     age += 1
# else:
#     print("Now you are welcome to become AQA Engineer!")



secret_number = 7
guess = randint(1, 20)

while True:
    if guess == secret_number:
        print("You won!")
        break
    else:
        print(f"{guess} Try again")
        guess = randint(1, 20)

