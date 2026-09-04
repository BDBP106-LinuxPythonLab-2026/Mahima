#!bin/bash

arg1=$1
arg2=$2
arg3=$3
arg4=$4



if [ -z $4 ];then
	$?=127
	echo "Exit code = $?"
else
	echo "Argument1 = $1"
        echo "Argument2 = $2"
        echo "Argument3 = $3"
        echo "Argument4 = $4"
fi

