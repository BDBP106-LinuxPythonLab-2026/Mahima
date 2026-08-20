#!bin/bash

echo "Enter Fiename:"
read file


#check if the file is there or not.

if [ -f $file ];then 
	echo "The file exists"
else
	echo "The file does not exist"
fi

#check if the file exists and is not empty.

if [ -s $file ];then
	echo "The file exists and has data"
else
	echo "The file is either empty or doesn't exist"
fi

#check if anything (file/directory/symlink/ect) exists

if [ -e $file ];then
	echo "$file exists"
else
	echo "$file doesn't exist"
fi


