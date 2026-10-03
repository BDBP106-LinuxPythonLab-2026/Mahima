"""find the even numbers in a list"""
L=[1,2,3,4,5,6,7]
e=[]
for i in L :
    if (i%2)==0 :
        e.append(i)

print("list:"+str(L))
print("Even numbers in the list are: "+str(e))


