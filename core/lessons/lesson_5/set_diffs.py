from ipaddress import ip_network

first_set = {1,2,3,4,5}
second_set = {3,4,5,6,7}



only_in_first_set = first_set - second_set
only_in_first_set_v2 = first_set.difference(second_set) # що є в першому, але нема в другому

only_in_second_set = second_set - first_set
only_in_second_set_v2 = second_set.difference(first_set) # що є в другому, але нема в першому


only_in_second_set_v3 = first_set.symmetric_difference(second_set) # outer


# print(only_in_first_set)
# print(only_in_first_set_v2)

print(only_in_second_set)
print(only_in_second_set_v2)
print(only_in_second_set_v3)


# -------------------------------
first_set = {1,2,3,4,5}
second_set = {3,4,5,6,7}

inner_join = first_set.intersection(second_set)
print(inner_join)


# --------------------------


set_of_numbers = {1,2,3,4,5, (3,4)}
set_2 = {3,4}


set_2_in_set_of_numbers = set_2.issubset(set_of_numbers)
print(set_2_in_set_of_numbers)



three_in_set_of_numbers: bool = (3, 4) in set_of_numbers
print("->", three_in_set_of_numbers)


for number in [3,4]:
    if number in set_of_numbers:
        print(f"{number} is in set_of_numbers")

if 3 in set_of_numbers:
    print("3 is in set_of_numbers")



is_subset_ = set([3,4,5]).issubset(set_of_numbers)
print(is_subset_)