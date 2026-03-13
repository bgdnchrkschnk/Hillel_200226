users_to_email = {"njkre", "bdjnc", "ue7823"}
print(type(users_to_email), users_to_email)

# ---------------------------- .add()

users_to_email.add("Nathan37")
users_to_email.add("Eij2778")
users_to_email.add("njkre")


print(type(users_to_email), users_to_email)

# ---------------------- .update()  |


my_set_1 = {1,2,3,4,5}
my_set_2 = {4,5,6,7,8}

my_set_1.update(my_set_2)
print(my_set_1)


my_set_3 = my_set_1 | my_set_2
print(my_set_3)


# ---------------------- .pop() видалити рандомний елемент та повернути його (return)
users_to_email = {"njkre", "bdjnc", "ue7823"}
removed_element = users_to_email.pop()

print(removed_element)
print(users_to_email)

# ----------------------- .remove (element) видалити конкректний елемент та БЕЗ повертання його

users_to_email = {"njkre", "bdjnc", "ue7823"}
users_to_email.remove("njkre")

print(users_to_email)

set_of_ids = {1,2,3,4,5,6,7,8,9,10}
processed_ids: set = set()
for id_ in set_of_ids:
    # email_sender.send_email(id)
    processed_ids.add(id_)

for processed_id in processed_ids:
    set_of_ids.remove(processed_id)
    print("Finally processed id: ", processed_id, end="")


# ---------------
# for _ in range(len(set_of_ids)):
#     id_to_process_= set_of_ids.pop()
#     set_of_ids.remove(id_to_process_)


