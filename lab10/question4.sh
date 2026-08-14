#1/bin/bash

echo -n 'Enter a number:'
read num

if [ "$num" -gt 0 ];then
	echo 'The number is positive.'
fi
if [ "$num" -lt 0 ];then
	echo 'The number is negative.'
fi
if  [ "$num" -eq 0 ];then
	echo "The number is equal to zero"
fi
