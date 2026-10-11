a=59
attempts=0
while attempts<7:
    b=int(input("Guess the number:"))
    attempts+=1
    if a==b:
        print('Yay! You guessed correctly!')
        break
    elif attempts==7:
        print("Too many attempts:The number is "+str(a))
    elif a>b:
        print("Too low")
    else:
        print("Too high")

print("Total attempts taken:"+str(attempts))




