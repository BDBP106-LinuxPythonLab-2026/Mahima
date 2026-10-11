d={"gfg":[5,7,7,7,7],"is":[6,7,7,7],"Best":[9,9,6,5,5]}
val=list(d.values())
key=list(d.keys())
maxuniq=set(val[0])
uniq=key[0]
for i in range(0,(len(val))):
    r=val[i]
    s=set(r)
    if len(s)>len(maxuniq):
        uniq=key[i]
        maxnuiq=r

print(uniq)

