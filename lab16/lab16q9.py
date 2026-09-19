a=int(input("Enter a number:"))
r=0

while a>0:
    r=((r*10)+(a%10))
    a=(a//10)

print("The reversed number is :"+str(r))