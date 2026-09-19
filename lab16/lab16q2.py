R=float(input("What is the interest rate?"))
P=float(input("What is the principle amount?"))
T=float(input("What is the time?"))

SI=((P*T*R)/100)
amount=(SI+P)
print("The simple interest is "+str(SI)+" and the total amount is "+str(amount))