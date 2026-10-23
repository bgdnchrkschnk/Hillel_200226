names = ["Bohdan", "Denys", "Andriy"]

# filter(Function(bool), iterable)
result = filter(lambda name: name.startswith('A'), names)
print(list(result))


filtered_names = [name for name in names if name.startswith('A')]
print(filtered_names)




transactions_data: list[dict] = [
    {"tran_id": 26772, "amount": 120.50, "user_id": 30, "status": "completed"},
    {"tran_id": 26773, "amount": -40.50, "user_id": 22, "status": "pending"},
    {"tran_id": 26771, "amount": -0.50, "user_id": 21, "status": "failed"},
    {"tran_id": 26774, "amount": 75.00, "user_id": 18, "status": "completed"},
    {"tran_id": 26775, "amount": -15.25, "user_id": 25, "status": "pending"},
    {"tran_id": 26776, "amount": 200.00, "user_id": 30, "status": "completed"},
    {"tran_id": 26777, "amount": -5.00, "user_id": 19, "status": "failed"},
    {"tran_id": 26778, "amount": 60.00, "user_id": 22, "status": "completed"},
    {"tran_id": 26779, "amount": -100.00, "user_id": 31, "status": "pending"},
    {"tran_id": 26780, "amount": 300.00, "user_id": 30, "status": "completed"},
    {"tran_id": 26781, "amount": -0.99, "user_id": 21, "status": "failed"},
    {"tran_id": 26782, "amount": 45.75, "user_id": 25, "status": "completed"},
    {"tran_id": 26783, "amount": -20.00, "user_id": 19, "status": "pending"},
    {"tran_id": 26784, "amount": 150.00, "user_id": 18, "status": "completed"},
    {"tran_id": 26785, "amount": -10.00, "user_id": 31, "status": "failed"}
]

blocked_users = {19, 21, 31}

def is_valid_transaction(tran: dict) -> bool:
    if tran["status"] != "completed":
        return False
    return True



filtered_transactions = list(filter(is_valid_transaction, transactions_data))
filtered_transactions_lc = [tran for tran in transactions_data if tran['status'] == "completed"]

print(filtered_transactions)
print(filtered_transactions_lc)