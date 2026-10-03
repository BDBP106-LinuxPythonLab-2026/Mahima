k=int(input("k :"))
L=[1,1,1,2,2,3,3,3,4,4,4,5,5,6,5,7,7,6,5,4,6,6,5,4,8,3,8,5,9,3,7,5]
e=set()


for i in range(0,len(L)):
    if L.count(L[i])>k:
        e.add(L[i])

print("list :"+str(L))
print("Elements repeated more than "+str(k)+" times :"+str(e))
