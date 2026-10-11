def greet_decorator(func):
    def wrapper():
        print("This the is the statement before the function.")
        func()
        print("This is the statement after the function.")
    return wrapper

@greet_decorator
def message():
    print("This is my first attempt at using decorator.")

message()