from functools import reduce

a=["A","p","p","l","e"," ",'i','s',' ','a',' ',"g","o","o","d"," ","f","r","u","i","t"]
b=reduce((lambda a,b: a+b) , a)
print(a)
print(b)