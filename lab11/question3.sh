#!bin/bash

echo "What is your name?"
read name

if [ -n "$name" ];then
	echo "My name is $name"
else
	echo "I don't want to tell my name."
fi


