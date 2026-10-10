n=int(input('Enter a number: '))
fibs=[]
a=0
b=1
for i in range(0,n):
    fibs.append(b)
    a,b=b,a+b
print(fibs)
odd=list(filter(lambda p: p%2!=0 , fibs))
print(odd)