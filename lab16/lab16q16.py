"""To determine the type of triangle"""
a=float(input("Side 1 = "))
b=float(input("Side 2 = "))
c=float(input("Side 3 = "))

if a == b and c :
    print("This is an equilateral triangle.")
elif a == b or a == c or b == c :
    print("This is an isosceles triangle.")
else :
    print("This is a scalene triangle.")