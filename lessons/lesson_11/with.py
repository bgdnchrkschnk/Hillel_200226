# file = open("assert.py", "r")
#
# print(file.read())
#
# ...
#
# file.close()
#
# file = None
# try:
#     file = open("assert2.py", "r")
#     file_data = file.read()
#     print(file_data)
# except Exception as e:
#     print(f"Something went wrong", e)
# finally:
#     if file is not None:
#         file.close()


with open("assert.py", "r") as file:
    file_data = file.read()
    print(file_data)

