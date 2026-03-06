welcome_message: str = "Welcome, Bohdan to portal!"

welcome_message_lower = welcome_message.lower()
welcome_message_upper = welcome_message.upper()
welcome_message_title = welcome_message.title()
welcome_message_capitalize = welcome_message.capitalize()


print(welcome_message_lower)
print(welcome_message_upper)
print(welcome_message_title)
print(welcome_message_capitalize)


name = "bohdan"

if name != name.title():
    print("Name format is not correct")

# ------------------------------------------

text_message = "Product price: 15 Usd"


if "USD" in text_message.upper():
    print("text message contains USD")

if "EUR" in text_message.upper():
    print("text message contains EUR")


print(
    "USD" in text_message.upper() # -> True/False
)



if "usd" in text_message.lower():
    print("text message contains usd")

if "eur" in text_message.lower():
    print("text message contains eur")



welcome_message: str = "WelCoMe, BOHDan to portal!"
normalized_message = welcome_message.capitalize()


print(normalized_message)
print(welcome_message)

# --------------------------------------------- is_lower, is_upper, is_digit, is_alpha, is_alnum, is_space -> bool

welcome_message_is_lower = f"message is lower: {welcome_message.islower()}" # -> чи строка з нижнього регістру
welcome_message_is_upper = f"message is upper: {welcome_message.isupper()}" # -> чи строка з верхнього регістру
welcome_message_is_digit = f"message is digit: {welcome_message.isdigit()}" # -> чи строка повністю з цифр
welcome_message_is_alpha = f"message is alpha: {welcome_message.isalpha()}" # -> чи строка повністю з літер та ЦИФр


print(welcome_message_is_lower)
print(welcome_message_is_upper)
print(welcome_message_is_digit)

welcome_message_is_alnum = welcome_message.isalnum()
welcome_message_is_space = welcome_message.isspace()

welcome_message_is_alnum: bool = welcome_message.isalnum()

print(welcome_message_is_alnum)



# ----------------------------------------

phone_number = "0987654321"

if phone_number.isdigit():
    print("phone number is saved in db")


space_string = "\t\t\n"
space_string_v2 = "                         "

print(
    space_string.isspace()
)

# ----------------------------------------- startswith, endswith -> bool

filename = "server_output.log"

is_log_file: bool = filename.endswith(".log") # чи закінчується строчка на певний патерн

print(is_log_file)

log_message = "INFO: Invalid input data"

is_error_message: bool = log_message.startswith("ERROR") # чи закінчується строчка на певний патерн
print(is_error_message)
