class User:

    def __init__(self, nickname, age, sex):
        self.nickname = nickname
        self.age = age
        self.sex = sex
        self.friends = []
        self.rating = 0

    def __str__(self): # for user
        return f"User: {self.nickname}, Age: {self.age}"

    def __repr__(self): # for dev (debug)
        return f"User={self.nickname}, Age={self.age}, Sex={self.sex}"

    def __len__(self):
        return len(self.nickname)

    def __gt__(self, other_user): # >
        return all([self.age > other_user.age, len(self.nickname) > len(other_user.nickname)])

    def __lt__(self, other_user): # <
        ...

    def __eq__(self, other): # ==
        print(f"Comparing {self.__dict__} and {other.__dict__}")
        return self.__dict__ == other.__dict__

    def __add__(self, other_user):
        # self.friends.append(other_user)
        # other_user.friends.append(self)
        if self.sex == "male" and other_user.sex == "male":
            raise PermissionError("You cannot marry two guys")

        self.is_married = True
        other_user.is_married = True

        print(f"User {self.nickname} and {other_user.nickname} are married")

    def __getattribute__(self, item): # get existing attribute
        if item == "is_married":
            raise PermissionError("User cannot see is_married attribute")

        print(f"Getting {item} attribute")
        return super().__getattribute__(item)

    def __getattr__(self, item) -> None: # get non-existing attribute
        print(f"Attribute {item} does not exist")

    def __setattr__(self, key, value):
        print(f"Setting {key} attribute with value {value}")
        if (key == "sex") and ("sex" in self.__dict__):
            raise PermissionError("Not supported to change sex")
        return super().__setattr__(key, value)

    def __delattr__(self, atribbute_name: str):
        print(f"Deleting {atribbute_name} attribute")
        return super().__delattr__(atribbute_name)


petro = User("Petro", 23, "male")
# petro_2 = User("Petro", 23, "male")
katya = User("Ekateryna", 22, "female")

# print(petro.nickname)
# print(katya.friends)
# # print(petro.is_married)
# print(petro_2.music_genre)
# print(petro_2.cv)
katya.music_genre = "Rock"
katya.music_genre = "Pop"
print(katya.sex)
print(katya.__dict__)
del katya.sex
print(katya.__dict__)




# len_of_petro = len(petro)
# len_of_ekateryna = len(katya)
#
# print(len_of_petro)
# print(len_of_ekateryna)
#
# print(
#     petro > katya, katya > petro, sep="; "
# )
#
# petro_eq_katya = petro == petro_2
# print(petro_eq_katya)
#
#
# petro + katya
# petro + petro_2
#
# print(petro.__dict__)

