def type_finder(a,b,c):
    if a==b and a==c:
        return "equilateral"
    elif (a==b and a!=c) or  (a==c and a!=b) or (b==c and b!=a):
        return "isosceles"
    elif a!=b and b!=c:
        return "scalene"


try1=type_finder(1,1,1)
print(try1)