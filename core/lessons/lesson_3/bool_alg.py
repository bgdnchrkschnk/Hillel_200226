


"""
True and True -> True
True and False -> False

True or True -> True
True or False -> True
False or True -> True
False or False -> False

not True -> False
not False -> True
"""

email_of_user = None

# if expression(True/False):


# if not email_of_user: # not(False) email is not None
#     print("User has no email")


# if email_of_user: # True bool(email_of_user)
#     print("User has email")


username = None
user_email = "hehwuh@asd.com"
user_password = ""

# Логіка реєстрації
if username and user_email and user_password:
    print("✅ Користувач зареєстрований")
elif username is None or user_password == "":
    print("⚠️ Реєстрація неможлива: відсутні обов'язкові дані")
else:
    print("ℹ️ Дані частково заповнені, потрібна перевірка")


