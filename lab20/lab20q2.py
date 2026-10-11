a=str(input("Enter a scentence:"))
vowels=0
consonants=0
digits=0
spaces=0
for i in a.lower():
    if i.isalpha():
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            vowels+=1
        else:
            consonants+=1
    elif i==" ":
        spaces+=1
    elif i.isalnum():
        digits+=1

print('Vowels: '+str(vowels)+" Consonants: "+str(consonants)+" Digits: "+str(digits)+" Spaces: "+str(spaces))