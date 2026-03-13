temperature = 13
is_raining = True # bool(False) -> False



# if temperature < 0:
#     print("Its very freezing. Take on hat and coat")
# else:
#     if temperature < 10:
#         print("Its getting cold. Take on coat")
#     else:
#         print("Its getting warm! T shirt is recommended")

if temperature < 0:
    print("Its very freezing. Take on hat and coat")
elif temperature < 10:
    print("Its getting cold. Take on coat")
elif temperature < 25:
    print("Its getting warm! T shirt is recommended")
else:
    print("Its very hot. Take on jacket")


# if temperature < 0:
#     print("Its very freezing. Take on hat and coat")
# if temperature > 10:
#     print("Its getting cold. Take on coat")
# if temperature > 25:
#     print("Its getting warm! T shirt is recommended")
# else:
#     print("Its very hot. Take on jacket")



if is_raining: # is_raining is True
    print("Its raining. Take umbrella!")



# -----------------------------------------------------

age = 15
name = "Maryana"
gender = "female"
user_id = 563

vip_list = [101, 102, 205, 563]


# дівчатам вхід з 18 - 250 uah
# чоловікам вхід з 16 - 500 uah
# віп заходять безкоштовно незалежно від віку


# True and True -> True
# True and False -> False

if (gender == "male") and (age >= 16): # if True/False
    entry_price = 500
    print(f"User {name} welcome to club! Entry: {entry_price} uah")
elif gender == "female" and age >= 18:
    entry_price = 250
    print(f"User {name} welcome to club! Entry: {entry_price} uah")
elif user_id and (user_id in vip_list):
    print(f"[VIP] User {name} welcome to club! Entry: free")
else:
    if gender == "male" and age < 16:
        print("Men are allowed only from 16, sorry")
    elif gender == "female" and age < 18:
        print("Women are allowed only from 18, sorry")


