import array
a=int(input("Enter a number:"))
sum=0
while a>0:
    sum=(sum+(a%10))
    a=(a//10)
print("The sum of the digits is:"+str(sum))