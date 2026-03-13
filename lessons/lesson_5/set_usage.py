list_of_transactions: list = [1245, 467, 334, 11, 467, 90, 11]

print(type(list_of_transactions), list_of_transactions)

print("First element: ", list_of_transactions[0])
print("Last element: ", list_of_transactions[-1])



# set - немає дублікатів (тільки унікальні значення)
set_of_transactions = set(list_of_transactions)


set_of_transactions.add(11)
print(type(set_of_transactions), set_of_transactions)

# print(set_of_transactions[0]) # неможливо взяти елемент по індексу

set_numbers: set = {1,2,3,0,26,-90}
print(set_numbers)


for number in set_numbers:
    print(number)


set_of_random_data = {"Bohdan", 29, 36.6, True, False, None, (1,2,3)} # only immutable data

# print(hash("Bohdan"))
# print(hash([1,2,3]))


# ---------------------------

expected_result = ["bhjc", "bhjca", "jnwef", "nkajcwef156"]

actual_result = ["bhjc", "bhjca", "jnwef", "nkajcwef156", "jnwef", "nkajcwef156"]

actual_result_is_equal_to_expected_result = len(set(actual_result)) == len(expected_result)

print(actual_result_is_equal_to_expected_result)



