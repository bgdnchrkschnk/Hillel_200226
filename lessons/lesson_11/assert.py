def average_value(list_of_number: list[int]):
    avg = sum(list_of_number) / len(list_of_number)
    return avg

test_data = [1,2,3,4,5]
expected_result = 3

# if average_value(test_data) != expected_result:
#     raise AssertionError("Average value is not equal to expected value")

assert average_value(test_data) == expected_result, "Average value is not equal to expected value" # assert condition
assert average_value([10,20,30]) == 20 , "Average value is not equal to expected value"


# assert False, "Some error"
assert True, "Some error"




