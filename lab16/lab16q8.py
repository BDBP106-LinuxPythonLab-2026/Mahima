a=float(input("x="))
b=float(input("y="))

if a>0 and b>0:
    print("The point lies in the first quadrant.")
elif a>0 and b<0:
    print("The point lies in the second quadrant.")
elif a<0 and b<0:
    print("The point lies in the third quadrant.")
elif a<0 and b>0:
    print("The point lies in the fourth quadrant.")