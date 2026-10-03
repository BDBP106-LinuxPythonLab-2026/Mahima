"""Check if word are anagram"""
a=str(input("Enter 1st word:"))
b=str(input("Enter 2nd word:"))

if sorted(a)==sorted(b):
    print("The words are anagrams of each other.")
else:
    print("The words are not anagrams of each other.")