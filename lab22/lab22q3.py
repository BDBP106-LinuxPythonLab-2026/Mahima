def count_calls(func):
    count=[0]

    def wrapper():
        count[0]+=1
        func()
        print("Count = "+str(count[0]))

    return wrapper

@count_calls
def say_hi():
    print("Hi!")

say_hi()
say_hi()
say_hi()