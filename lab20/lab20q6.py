students=[("Asha",88),("Ravi",72),("Meera",72),("Karan",59),("Divya",81)]
for i in range(0,len(students)):
    if students[i][1]>=90:
        print(students[i][0]+": A")
    elif students[i][1]>=80:
        print(students[i][0]+": B")
    elif students[i][1]>=70:
        print(students[i][0]+": C")
    elif students[i][1]>=60:
        print(students[i][0]+": D")
    else:
        print(students[i][0]+": F")

top=0
bottom=0
total=0

for i in range(0,len(students)):
    if students[top][1]<students[i][1]:
        top=i
        total+=students[i][1]
    elif students[bottom][1]>students[i][1]:
        bottom=i
        total+=students[i][1]
    else:
        total+=students[i][1]


print("Top scorer is :"+str(students[top][0])+str(students[top][1]))
print("Bottom scorer is :"+str(students[bottom][0])+str(students[bottom][1]))
print("The class average is :"+str(total/len(students)))