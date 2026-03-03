my_string: str = "Привіт, світ!"

encoded_string = my_string.encode(encoding="windows-1251")
decoded_string = encoded_string.decode(encoding="windows-1251")


print(decoded_string)