import numpy as np
print(np.__version__)

#i
a=np.arange(10)
print(a)

#ii
b=np.ones((3,3),dtype=np.bool)
print(b)
c=np.zeros((3,3),dtype=np.bool)
print(c)

#iii
arr=np.arange(1,51)
print(arr)
arr=arr[[all(d%i!=0 for i in range(2,int(d/2+1))) and d>1for d in arr ]]
#arr = arr[[all(i % d != 0 for d in range(2, int(i**0.5) + 1)) and i > 1 for i in arr]]
print(arr)

#iv
rg=np.random.default_rng(100)
d=rg.random((20))
print(d)
e=d.reshape(4,5)
print(e)

#v
a=np.arange(10)
print(a)
b=np.ones((10),dtype=int)
print(b)
c=np.hstack((a,b))
print(c)

#vi
a1=np.arange(1,101)
print(a1)

def isprime(x):
    res=True
    for i in range(2,int(x/2)+1):
        if x%i==0:
            res=False
            break
    return res

p=[i for i in range(2,545) if isprime(i)]
a2=np.array(p)
print(a2)
inter=np.intersect1d(a1,a2)
print(inter)

#vii
uniq=np.setdiff1d(a1,a2)
print(uniq)

#viii
c=np.where(a1==a2)  #gives index if same elements at the same index
print(c) #no same value therefore empty list as output

#ix
a3=a1[5<a1]
a3=a3[20>a3]
print(a3)