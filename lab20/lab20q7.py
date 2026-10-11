a=str(input("Enter a paragraph:"))
b=a.split()
c=[(word.strip(".,!?:;")).lower() for word in b]

d={}
s=sorted(c)

for i in range(0,len(s)):
    d[s[i]]=s.count(s[i])

print(d)

m=max(d.values())

for key,values in d.items():
    if values==m:
        print(key,values)
