a=float(input("a = "))
b=float(input("b = "))
c=float(input("c = "))

D=((b**2)-(4*a*c))

if D<0 :
    print("This equation has no real roots.")
elif D==0 :
    root=((-b)/(2*a))
    print("The root is : "+str(root))
else :
    root1=((-b+(D**(1/2)))/(2*a))
    root2=((-b-(D**(1/2)))/(2*a))
    print("The roots are "+str(root1)+" and "+str(root2))