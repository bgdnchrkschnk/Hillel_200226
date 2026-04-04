# LEGB   Local/Enclosing(nonlocal)/Global/Built-In

string = "Global"

def outer():

    string = "Nonlocal"

    def inner():

        string = "Local"

    print(string)
    inner()

outer()