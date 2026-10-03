"""to print duplicate elements in a list"""
L=[1,2,3,4,5,6,7,8,9,1,2,4,7,0,4]
K=set()

for i in range(0,len(L)) :
    for j in range(i+1,len(L)):
        if L[i]==L[j]:
            K.add(L[i])


print("List: "+str(L))
print("Duplicates Elements: "+str(K))