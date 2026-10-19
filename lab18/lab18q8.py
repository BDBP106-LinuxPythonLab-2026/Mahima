a=[23,32,33,44,'BDBH101','hello','python', 15, 1e-10, True,'hit']
print("Before : ",a)
for i in range(0,len(a)):
    if i%2==0:
        if i+1==len(a):
            pass
        else:
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp

print("After : ",a)