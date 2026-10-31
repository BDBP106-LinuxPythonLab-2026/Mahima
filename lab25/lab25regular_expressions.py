#regular expression
import re

# question3. to get 000 - 255
#  ^([01]\d{2}|2[0-4]\d|25[0-5])$
test1=["255","000","143","99","7","714",'0']
#test="\n".join(test)
#print(re.findall("^([01]\\d{2}|2[0-4]\\d|25[0-5])$","255"))
print("question 3:")
for i in range(len(test1)):
    print(re.findall("^([01]\\d{2}|2[0-4]\\d|25[0-5])$",test1[i]))


#question4. to get 0-255
# ^(\\d{1,2}|[0-1]\\d{2}|2[0-4]\\d|25[0-5])$
print("question 4:")
for i in range(len(test1)):
    print(re.findall("^(\\d{1,2}|[0-1]\\d{2}|2[0-4]\\d|25[0-5])$",test1[i]))

#question5, to get an email address
# (\\w+@[a-zA-Z]+(?:\\.[a-zA-Z]+)+)
print("Question 5:")
test2="My personal email address is abc780@gmail.com and my student email address is abc014@ibab.ac.in , an extra email id is abc780@gmail.com ."
print(re.findall("(\\w+@[a-zA-Z]+(?:\\.[a-zA-Z]+)+)",test2))


#question6, to check if a line of csv file contains an email address in its third field
# ^[\\w\\W\\s\\S]+,[\\w\\W\\s\\S]+,(\\w+@[a-zA-Z]+(?:\\.[a-zA-Z]+)+),[\\w\\W\\s\\S]+$
print("Question 6:")
test3="Mahima Shuka,22,mahi_ma@ibab.ac.in,bunch,of, stuff,"
print(re.findall("^[\\w\\W\\s\\S]+,[\\w\\W\\s\\S]+,(\\w+@[a-zA-Z]+(?:\\.[a-zA-Z]+)+),[\\w\\W\\s\\S]+$",test3))

#question7. to check for all unique email addresses
print("Question 7:")
all=re.findall("(\\w+@[a-zA-Z]+(?:\\.[a-zA-Z]+)+)",test2)
print(set(all))

#question8 ,to search for email addresses and mask it out
# "(\\w)(\\w*)(\\w)@([a-zA-Z]+\\.[a-zA-Z]{2,})"
print("Question 8:")
def mask_email(match):
    first=match.group(1)
    last=match.group(3)
    middle="*" * len(match.group(2))
    domain=match.group(4)
    return first+middle+last+"@"+domain
print(re.sub("(\\w)(\\w*)(\\w)@([a-zA-Z]+\\.[a-zA-Z]{2,})",mask_email,test2))

#question9 ,to search for EcoRI site in given DNA sequence
print("Question 9:")
print(re.search("GAATTC","ATCGCGAATTCAC").group())

#question10 , to check for AvaII site in DNA sequence
print("Question 10:")
print(re.search("GGACC|GGTCC","ATCGCGAATTCAC"))

#Question11, to check for BisI site in DNA sequence
print("Question 11:")
print(re.search("GC[ATGC]GC","ATCGCGAATTCAC"))

#question12, to check for bases that are not  A,T,G,C
print("Question 12:")
print(re.findall("[^ATGC]","ATCGCGYAATTCAC"))

#question 13, to split a dna where the base is not A,T,G,C
print("Question 13:")
print(re.split("[^ATGC]","ACTNGCATRGCTACGTYACGATSCGAWTCG"))