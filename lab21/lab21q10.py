a=input("Enter a string: ")
b=list(filter((lambda b: b in "aeiouAEIOU"), a.lower()))
print("".join(b))