from functools import reduce


l=[1,2,3,4,5,6,6,7,4,3]
s=reduce((lambda a, b: a+b ),l,0)

print("list: "+str(l))
print("sum = "+str(s))