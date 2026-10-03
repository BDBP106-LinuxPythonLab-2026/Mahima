a=[[4,50,6],[3,445,67]]
b=[[2,6,5],[1,99,5]]
c=[]
d=[]
e=[c,d]


for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        e[i].append(a[i][j]-b[i][j])

print(str(a)+"-"+str(b)+"="+str(e))
