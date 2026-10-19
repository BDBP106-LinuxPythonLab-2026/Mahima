def nextprime(n):
    num=n+1
    while True:
        for i in range(2,num):
                if num%i==0:
                    break
        else:
            return num
        num+=1

m=int(input("Enter an integer: "))
o=nextprime(m)
print("The next prime number is :",o)