"""remove particular element from list"""
l=[1,2,3,4,5,5,6,7,8,9,10,11,1,2,1,3,14]
print(l)
a=int(input("Choose a number to remove: "))
for i in l:
    if i==a:
        l.remove(i)

print(l)