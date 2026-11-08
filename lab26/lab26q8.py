import numpy as np

a=np.random.randint(10,40,10)
print("array: ",a)
print("avg: ",np.average(a))
print("max :",np.max(a))
print("min :",np.min(a))
print("Numbers smaller than 20: ",a[a<20])
print('Numbers greater than 20: ',a[a>20])