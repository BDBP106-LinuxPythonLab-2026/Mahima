n=int(input("n : "))
h=[str(i) for i in range(1,n+1)]
sh=(" ".join(h)).rjust(9)
print(sh)
for i in range(1,n+1):
    m=[str(i*j) for j in range(1,n+1)]
    o=" ".join(m)
    print(i,o)

























