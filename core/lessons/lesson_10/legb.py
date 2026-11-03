# LEGB   Local/Enclosing(nonlocal)/Global/Built-In

string = "Global"

def outer():

    string = "Nonlocal"

    def inner():
        global string
        string = "Local"

    inner()

outer()
print(string)