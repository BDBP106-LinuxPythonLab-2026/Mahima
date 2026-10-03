#i
a=[i for i in range(1,51)]

s=sum([i for i in a])
print("sum: "+str(s))

#ii
def prime(a):
    res=True
    for i in range(2,a):
        if a%i==0:
            res=False
            break
    return res
b=[j for j in range(2,51) if prime(j)]
print("b :"+str(b))

#trial 2
b=[i for i in range(2,51) if all(i % n !=0 for n in range(2,i))]



#iii
c=[j for i in a for j in b if j==i]
print("c :"+str(c))