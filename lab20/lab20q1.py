a=int(input("enter a integer :"))

if a==0:
    print("Zero")
elif a>0:
    if a%2==0:
        print("Positive,Even")
    else :
        print("Positive,Odd")
else:
    if a%2==0:
        print("Negative,Even")
    else:
        print("Negative,Odd")


if a%5==0 and a%3==0:
    print("FizzBuzz number!")