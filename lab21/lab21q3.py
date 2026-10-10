"""Convert a tuples of angles into list of tuples of their sin and cos value"""
import math

def trig(x):return math.sin(x),math.cos(x)  #angles in radian, for angle in degree  do convert it into radian before putting it in sin function
list1=[1,5,0,3.14,6.28]
list2=list(map(trig,list1))
print(list2)

#lambda form of the same code as above
list4=[90,60,45,30,0]
list3=list(map(lambda x : (math.sin(math.radians(x)), math.cos(math.radians(x))),list4))
print(list3)
