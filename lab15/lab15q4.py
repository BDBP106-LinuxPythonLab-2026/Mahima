#question4
#find and print the roots

a=float(input("Enter a number:"))
b=float(input("Enter a number:"))
c=float(input("Enter a number:"))

root1=(-b+(((b**2)-(4*a*c))**(1/2)))/(2*a)
root2=(-b-(((b**2)-(4*a*c))**(1/2)))/(2*a)

print("The root of equation is "+str(root1)+"and "+str(root2))
