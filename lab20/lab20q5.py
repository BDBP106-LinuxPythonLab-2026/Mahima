menu=[]
op=["Add item","Remove item","View list","Sort list","Quit"]
todo=1
ip=""
while ip!=op[4]:
    print("Options="+str(op))
    ip=input("Choose a task:")
    if ip==op[0]:
         a=str(input("Enter item name:"))
         for i in menu:
             if i.lower()==a.lower():
                 print("The item is already on list.")
                 todo=0
                 break
         if todo:
             menu.append(a)
             print('Item added')
         else:
             todo=1
    elif ip==op[1]:
         b=str(input("Enter item name:"))
         menu_lowercase = [i.lower() for i in menu]
         if b.lower() in menu_lowercase:
             menu.remove(b)
             print("Item removed")
         else:
             print("Error:Trying to remove a item which is not there")
    elif ip==op[2]:
         for i in range(0,len(menu)):
             print(str(i+1)+". "+str(menu[i]))
    elif ip==op[3]:
         print(sorted(menu))
    else:
        print("Error: invalid task chosen")



