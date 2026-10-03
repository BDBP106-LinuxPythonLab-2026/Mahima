#i
a=[i for i in range(1,51)]
#ii
print(1,a[1:5])     #added numbers to improve readability of the results
print(2,a[3:20:2])
print(3,a[::2])
print(4,a[::])
print(5,a[10::2])
print(6,a[1:1:1])
print(7,a[:0:])
print(8,a[-7::1])
print(9,a[-6:])
print(10,a[-10:-4])

#iii
print(11,a[::-1])
print(12,a[::-3])
print(13,a[:1:-2])
print(14,a[-1:-1:-1])
print(15,a[:-5:-1])
print(16,a[:0:-1])
print(17,a[:-1:-1])
print(18,a[0:-5:-1])
print(19,a[-1:5:-1])
print(20,a[2:2:-1])
print(21,a[2:1:-1])
print(22,a[0:-5])


#iv
b=[i for i in a[1::2]]
print("even number list:"+str(b))
c=[i for i in a[0:10]]
d=[i for i in a[35:50:2]]
c.extend(d)
print("The new list is:" +str(c))






