#i
a=[i for i in range(1,51)]
A=','.join([str(a[i]) for i in range(0,len(a))])
print("a:"+A)
b='.'.join([str(a[i]) for i in range(0,len(a))])
print("b:"+b)
c='-'.join([str(a[i]) for i in range(0,len(a))])
print("c:"+c)
sq=[i*i for i in a]
d="\n".join([" ".join([str(a[i]),str(sq[i])]) for i in range(0,len(a))])
print(d)

#ii
n=["mahima shukla","manekha verma",'tanishq kokate',"mahaprasad nayak","kaumudi priyadarshani","sneha bhattacharya","shravan pawale","sanjana pillai","ishika pandey","aashi dubey"]
uc=[i.upper() for i in n]
print(uc)

swp=[" ".join([name.split()[1],name.split()[0]]) for name in n]
print(swp)

fl=[".".join([(p.title()).split()[0],(p.title()).split()[1]]) for p in n]
print(fl)

#iii
s="she sells sea shells that she collects from the sea floor"
longestword=[max([word for word in s.split()], key=len)]
print("The longest word is :"+str(longestword))

#iv
rw=[s.split()[i] for i in range(0,len(s.split())) for j in range((i+1),len(s.split())) if s.split()[i]==s.split()[j]]
print("The repeated words are: "+str(rw))

