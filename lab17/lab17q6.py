"""Print alternate character"""

a=str(input("Enter a string : "))
b=''

for i in range(0,len(a),2):
    b+=(a[i])

print(b)