import math

angle=int(input("Enter the angle:"))
radian=(angle/180*math.pi)

sin=float(math.sin(radian))
cos=float(math.cos(radian))
tan=float(math.tan(radian))
cot=float(1/tan)
sec=float(1/sin)
cosec=float(1/cos)

print("sin("+str(angle)+")="+str(sin))
print("cos("+str(angle)+")="+str(cos))
print("tan("+str(angle)+")="+str(tan))
print("cot("+str(angle)+")="+str(cot))
print("sec("+str(angle)+")="+str(sec))
print("cosec("+str(angle)+")="+str(cosec))
