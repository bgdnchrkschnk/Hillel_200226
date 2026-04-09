class IsAdultFunctionError(BaseException):
    ...



def is_adult(age: int) -> None:
    if isinstance(age, int) or isinstance(age, float): # if type(age) not in (int, float) -> raise IsAdultFunctionError
        if age >= 18:
            print("Adult")
        else:
            print("Child")
    else:
        raise IsAdultFunctionError("Something went wrong")


is_adult(None)
