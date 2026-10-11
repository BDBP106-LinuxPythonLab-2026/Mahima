import time
import math

def measure_time(func):
    def wrapper(*args,**kwargs):
        begin=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        time_taken=end-begin
        print("Time taken to run the function :"+str(time_taken))
        return result
    return wrapper


@measure_time
def population_growth(initial,rate,time):
    def exponential_growth(i,r,t):
        for a in range(1000000):
            pop=i+math.e**(r*t)
        return pop
    nt=round(exponential_growth(initial,rate,time))

    return nt

N=population_growth(10,2,10)
print("Population after time : ",N)