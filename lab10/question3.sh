#!/bin/bash

echo "Enter filename:"
read file

if [ -f $file ];then
	if [ -x $file ];then
		echo "The file exists and it is executable."
	else
		echo "The file exists but it is not executable."
	fi
	exit 200
	exit $?
else
	echo "The file does not exist."
	exit 201
	echo $?
fi

echo "outside the if-block"
