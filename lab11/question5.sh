#!bin/bash

#1
var1=Testing
var2=testing


#2

if [ $var1 \> $var2 ];then
	echo "$var1 is greater than $var2"
else
	echo "$var1 is lesser than $var2"
fi


#3
#Testing is lesser than testing.


#4
echo "$var1" > teststringfile
echo "$var2" >> teststringfile


#5
sort teststringfile
#Testing is greater than testing
#The result of sort is opposite from if. The sort treats the uppercase as greater than lowercase, whereas, the if treats the lowercase as greaterthan the uppercase by default.
