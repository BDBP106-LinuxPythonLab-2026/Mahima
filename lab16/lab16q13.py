a=int(input("Enter a number:"))

c=a
b=1
if a>0:
    while a>0 :
        b=(b*a)
        a=(a-1)
    print(str(c)+"! = "+str(b))
else:
    print("ERROR:Negative numbers do not have a standard factorial value")