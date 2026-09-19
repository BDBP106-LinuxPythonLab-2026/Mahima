"""To calculate the distance between two points"""

a=float(input("x1 = "))
b=float(input("y1 = "))
c=float(input("x2 = "))
d=float(input("y2 = "))


r=((((a-c)**2)+((b-d)**2))**(1/2))

print("The distance between two points is : "+str(r))
