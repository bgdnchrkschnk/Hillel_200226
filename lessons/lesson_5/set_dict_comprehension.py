set_of_numbers_ = {number**2 for number in range(1,11) if number % 2 == 0} # set comprehension

print(set_of_numbers_)



# -----------------------------
dict_of_numbers_: dict = {number:number**2 for number in range(1,11)} # dict comprehension

print(dict_of_numbers_)


payments = [
    {"payment_id": "payment1", "status": "success"},
    {"payment_id": "payment1", "status": "success"},
    {"payment_id": "payment1", "status": "failed"},
    {"payment_id": "payment1", "status": "pending"},
    {"payment_id": "payment1", "status": "success"},
]


#
not_successfull_payments = [payment for payment in payments if payment['status'] != "success"]

print(not_successfull_payments)

# -----------
final_dict = {}
for payment in payments:
    if payment['status'] != "success":
        final_dict[payment['status'] + "_payments"] = payment

print(final_dict)

payments_to_reprocess = {payment['status'] + "_payments": payment for payment in payments if payment['status'] != "success"}
print(payments_to_reprocess)


# -------

statuses = {
    "payment1": "success",
    "payment2": "failed",
    "payment3": "success",
    "payment4": "pending"
}

only_successfull_payments = {payment: status for payment, status in statuses.items() if status=="success"} # dict

print(only_successfull_payments)







