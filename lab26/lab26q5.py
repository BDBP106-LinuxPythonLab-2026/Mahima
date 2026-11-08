import numpy as np
def max_ar(a1,a2):
    a3=np.array([np.max(a1),np.max(a2)])
    return a3

a=np.array([1,2])
b=np.array([0,5])

c=max_ar(a,b)
print(c)