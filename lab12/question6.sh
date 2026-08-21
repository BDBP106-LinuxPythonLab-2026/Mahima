#!/bin/bash

function maximum {
	var1=$1
	var2=$2
	if [ $var1 -gt $var2 ];then
		echo "The maximum is $var1"
	else
		echo "The maximum is $var2"
	fi
}

result=$(maximum $1 $2)
echo $result
