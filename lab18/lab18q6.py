"""calculate area of a triangle"""
def area(a,b,c):
    s=(a+b+c)/2
    ar=1/2**(s*(s-a)*(s-b)*(s-c))
    return ar

tri1=area(3,5,9)
print(tri1)