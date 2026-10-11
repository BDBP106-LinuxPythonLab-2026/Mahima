def check_positive(func):
    def wrapper(n):
        if n>0:
            func(n)
        else:
            print("The number must be positive!")
    return wrapper

@check_positive
def find_squareroot(n):
    r=math.sqrt(n)
    print("Square Root: "+str(r))

import math

find_squareroot(4)