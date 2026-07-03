number_string = "123"
number_2_string = "234"


float_string = "123.2"
float_2_string = "234.5"


result = int(number_string) + int(number_2_string)
result_2 = float(float_string) + float(float_2_string)
print(result)
print(result_2)


# рядок = "1,2,3,4,5"
# список = рядок.split(',')
# print(список)



# ----------------------------------

empty_string = ""
not_empty_string = " "
false_string = "False"
true_string = "True"


bool_ = bool(empty_string) # ---------> пуста
bool_2 = bool(not_empty_string) # -----> НЕ пуста

print(bool_)
print(bool_2)
print(bool(false_string))
