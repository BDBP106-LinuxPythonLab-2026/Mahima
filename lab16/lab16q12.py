"""Check if a string is a palindrome"""
a=str(input("Enter a string : "))
length=len(a)
b=""
l=(length-1)

for i in range(l,-1,-1):
    b += a[i]

if a==b:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")