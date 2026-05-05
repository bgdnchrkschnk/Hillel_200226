# <iterable>
# list, set, tuple, str, range

list_of_numbers = ["one","two","three","four","five"]

for element in list_of_numbers: # iter(list_of_numbers)
    print(element)


my_iterator = iter(list_of_numbers) # __next__

first_element = next(my_iterator)
second_element = next(my_iterator)
third_element = next(my_iterator)

print(first_element, second_element, third_element)

print(
    next(my_iterator)
)
print(
    next(my_iterator)
)

try:
    print(next(my_iterator))
except StopIteration:
    print("No more elements")

#
#
# class MyIterator:
#     def __init__(self, max_num):
#         self.max_num = max_num
#         self.current = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < self.max_num:
#             self.current += 1
#             return self.current
#         else:
#             raise StopIteration
#
# # Використання власного ітератора
# my_iterator = MyIterator(10)
# for num in my_iterator:
#     print(num)
#
#
