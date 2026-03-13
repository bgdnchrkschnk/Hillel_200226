# for
from lessons.lesson_6.if_bools import list_of_data

transactions_data: list[dict] = [
    {
        "tran_id": 26772,
        "amount": 120.50,
        "user_id": 30,
    },
    {
        "tran_id": 26773,
        "amount": 40.50,
        "user_id": 22,
        "status": "completed"
    },
    {
        "tran_id": 26771,
        "amount":  0.50,
        "user_id": 21,
        "status": "failed"
    },
    {
        "tran_id": 26771,
        "amount": -0.50,
        "user_id": 21,
        "status": "suspicious"
    },
    {
        "tran_id": 26781,
        "amount":  90.2,
        "user_id": 20,
        "status": "completed"
    }
]

completed_transactions = []
not_completed_transactions = []
ban_list = [20, 333, 177]

for transaction_dict in transactions_data:

    if transaction_dict.get("status") == 'suspicious':
        print("Transaction is suspicious! Ban user!")
        completed_transactions.clear()
        not_completed_transactions.clear()
        break

    if transaction_dict.get("user_id") in ban_list:
        print(f"User {transaction_dict.get('user_id')} is banned!")
        continue # skip this iteration

    if transaction_dict.get("amount") < 0:
        print(f"Transaction {transaction_dict['tran_id']} has negative amount!")
        continue

    if transaction_dict.get("status") == 'completed':
        print(f"Transaction {transaction_dict['tran_id']} completed successfully!")
        completed_transactions.append(transaction_dict)
    else:
        print(f"Transaction {transaction_dict['tran_id']} not completed! Status: {transaction_dict.get('status', "No status for some reason")}")
        not_completed_transactions.append(transaction_dict)
else: # якщо цикл пройшов повністю
    print("All transactions analyzed successfully")
print(completed_transactions)
print(not_completed_transactions)



list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# for number in list_of_numbers:
#     print(number)
#     if number == 5:
#         break
# else:
#     print("Report is successfully generated and sent to the user")


range_of_numbers = range(1,11)

# for i in range_of_numbers:
#     if i == 5:
#         continue # пропускає елемент
#     print(i)
#
#
# for i in range_of_numbers:
#     if i == 5:
#         break # зупиняє цикл
#     print(i)
#


tables = {
    "Стіл 1": ["Анна", "Іван"],
    "Стіл 2": ["Оля", "Петро", "Марія"],
    "Стіл 3": ["Сергій"]
}


for table, guests in tables.items():
    print(table)
    for guest in guests:
        print(guest)




print(
    type("hjagf") == int
)