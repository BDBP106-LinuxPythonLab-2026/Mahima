import time
from functools import reduce
def measure_time(func):
    def wrapper(n):
        begin=time.time()
        func(n)
        end=time.time()
        time_taken=end-begin
        print("Time taken to run the function :"+str(time_taken))
    return wrapper

@measure_time
def factorial(n):
        f=reduce((lambda x,y: x*y),range(1,n+1),1)
        print(f)


factorial(50)