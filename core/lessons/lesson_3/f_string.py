
my_name = "Bohdan"
my_age = 29
my_friends = ["Oleg", "Ivan"]
time_ = "12:30"


my_biography = f"My name is {my_name}, I am {my_age} years old, and my friends are {", ".join(friend for friend in my_friends)}. Timestamp: {time_} I am happy {not False}"

print(my_biography)

print(*my_friends)
print("Oleg", "Ivan")
# print(arg, arg, arg)