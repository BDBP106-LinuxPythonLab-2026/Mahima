#!/bin/bash

echo "Enter Number:"
read number
n=1

until [ "$n" -gt 15 ]
do
	echo "$[ $n * $number ]"
	n=$[$n+1]
done
