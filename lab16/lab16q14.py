'''To print fibonacci numbers till f25'''
a=1
b=a
c=2
print("f0 = 0")
print("f1 = 1")
while c<=25:
    print("f" + str(c) + " = " + str(b))
    a,b=b,b+a
    c=(c+1)