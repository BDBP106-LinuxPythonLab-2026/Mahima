a=str(input("Enter a sentence:"))
b=a.split()
c={}
for i in range(0,len(b)):
    c[b[i]]=i

print(" ".join(c.keys()))



