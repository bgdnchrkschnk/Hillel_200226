"""
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
"""

# +       -       *       **      /       //      %

print("sum", 1245 + 5765)
print("diff", 1245 - 5765)
print("mult", 1245 * 5765)
print("pow", 25 ** 3)
print("pow 2", pow(25, 3))

print(12 / 5) # -> float
print(12 // 5) # -> int  int(float) # банківське округлення

print(12 % 5) # 5 + 5 + 2
print(21 % 10) # 10 + 10 + 1


# банківське округлення (до найближчого парного)
# 2.5 -> 2
# 3.5 -> 4
# decimal


list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in list_of_numbers:
    if number % 2 == 0:
        print(f"ЧИСЛО ПАРНЕ: {number}")


# print("What is your name? ", number := input("What is your number? "))


# print(arg, arg, arg)
# print(arg)


# <       >       <=      >=      ==      !=


my_age = 29
club_access = 18

print(my_age < club_access) # False
print(my_age > club_access) # True
print(my_age <= club_access) # False
print(my_age >= club_access) # True
print(my_age == club_access) # False (equal)
print(my_age != club_access) # True (not equal)

print(not my_age == club_access) # True (not equal)

f"SELECT * FROM users WHERE age=18;"



# float


a = 0.1
b = 0.2
result = a + b

print(result)

# --------------------------------- decimal - better version of float

from decimal import Decimal

a = Decimal("0.0001")
b = Decimal("0.0002")
result = a + b
print(result)