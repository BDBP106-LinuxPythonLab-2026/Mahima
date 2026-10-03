"""Count the number of times W word appears in sentence S"""
S=str(input("Enter a sentence:"))
W=str(input('Enter word:'))

c=S.count(W)
print(W+" occurs "+str(c)+" times in the sentence.")