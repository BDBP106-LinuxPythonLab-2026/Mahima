"""To convert celsius into fahrenheit"""
def converter(x): return (x*9/5)+32
C=[2,37,25,-1,0,100]
F=list(map(converter,C))
print(F)
