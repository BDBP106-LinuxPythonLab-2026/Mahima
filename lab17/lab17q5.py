"""To halve a string"""
a=str(input("Enter a string : "))
b=""

for i in range(0,int(len(a)//2)):
    b+=(a[i])

print(b)