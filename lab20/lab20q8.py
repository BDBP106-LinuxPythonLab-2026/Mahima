python_class = ["Anil", "Bina", "Chetan", "Deepa", "Anil", "Esha"]
java_class = ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]
python=set(python_class)
java=set(java_class)
print("Students attending both classes: "+str(python.intersection(java)))
print("Students attending only python: "+str(python))
print("Students taking only one course: "+str(python^java))
print("All students: "+str(sorted(python.union(java))))

name=input("Enter a name:")
if name in python.intersection(java) :
    print("This student is enrolled in both the courses.")
elif name in python:
    print("This student is enrolled in python course.")
elif name in java:
    print("This student is enrolled in java course.")
else:
    print("Error : invalid name")