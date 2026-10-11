"""password"""
todo=[1]
while todo:
    todo=[]
    password=input("Enter a password(It should contain 8 characters, an upper case, a lower case,a special character,and no spaces):")
    if len(password)<8:
        print("The password is too short! Try again!")
        todo.append(1)
    if any(c.isupper() for c in password) and any(d.islower() for d in password) and any(e.isdigit() for e in password):
        pass
    else:
        print("The password is missing an uppercase or lowercase or digit character!Try again!")
        todo.append(1)
    if ("".join(password.split())).isalnum():
        print("The password should have a special character! Try again!")
        todo.append(1)
    if len(password)>len("".join(password.split())):
        print("The password cannot contain spaces!Try again!")
        todo.append(1)
    if password.lower()=="password":
        print("The password cannot be the word password!Try again!")
        todo.append(1)

print("Password saved successfully!")

