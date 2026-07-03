
def pre_conditions(func):
    def wrapper(*args, **kwargs):
        print(f"Precondition: decorator is working")
        func_result: int = func(*args, **kwargs) # 25
        return func_result
    return wrapper

def deco_double(func):
    def wrapper(number):
        func_result = func(number)
        return func_result * 2
    return wrapper


@pre_conditions
def hello():
    print("Hello")

@pre_conditions
def hello_2():
    print("Hello 2")

@pre_conditions
def hello_name(name, surname, age) -> None:
    print(f"Hello, {name} {surname} {age}")


@deco_double
@pre_conditions
def square(number) -> int:
    return number ** 2


print(square(5))


