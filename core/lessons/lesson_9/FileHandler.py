from typing import AnyStr

from utils.date_time import DatetimeUtils


class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = open(filename, mode)

    def read_data(self):
        return self.file.read()

    def __del__(self):
        print(f"File {self.filename} has been closed.")

    def print_date_now(self):
        print(DatetimeUtils.date_now())

    def close_file(self):
        self.file.close()


# file = open("/Users/milanstar/PycharmProjects/Hillel_200226/tst.py", "r") # open file
# file.read() # read file
# file.close() # close file

file = FileHandler(filename="/tst.py", mode="r")
data = file.read_data()
print(data)

del file
# file.close_file()

