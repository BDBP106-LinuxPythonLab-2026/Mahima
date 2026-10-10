import math

def population_growth(initial,rate,time):
    def exponential_growth(i,r,t):
        return i+math.e**(r*t)
    nt=round(exponential_growth(initial,rate,time))
    print(nt)

N=population_growth(10,2,10)
print(N)