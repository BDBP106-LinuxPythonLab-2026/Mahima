#!bin/bash

val1=Mahima
val2=Shukla

#if [ $val1 > $val2 ];then 
if [ $val1 \> $val2 ];then                    #this time the > symbol will not be interpreted as the redirection function; as the "\" before it tels the bash to ignore it.
	echo "$val1 is greater than $val2"
else

	echo "$val1 is lesser than $val2"
fi
