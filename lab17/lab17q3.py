N=int(input("Enter a number : "))
res=False

for i in range(2,int(N/2+1)):
    if (N%i)==0:
        res=True
        break

if res:
    print("N is not a prime number.")
else:
    print("N is a prime number.")