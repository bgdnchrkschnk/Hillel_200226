#range
range_of_numbers_0_10: range = range(11) # -> range object
range_of_numbers_only_not_even: range = range(1,11,2)

list_of_numbers = list(range_of_numbers_0_10)
list_of_numbers_2 = list(range_of_numbers_only_not_even)


#

only_not_even = []
for element in list_of_numbers:
    if element % 2 == 1:
        only_not_even.append(element)
print(only_not_even)

# list comprehension filtration
lc_not_evens = [element for element in list_of_numbers if element % 2 == 1]
print(lc_not_evens)

list_range_of_evens = [number for number in range(11) if number % 2 == 0]
print(list_range_of_evens)

