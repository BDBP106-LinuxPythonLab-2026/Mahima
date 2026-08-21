#!/bin/bash

read -ra numbers < nums.txt

echo ${numbers[*]}

for i in ${numbers[*]}
do
	echo "$[ i * 2 ]"
done

