#!/bin/bash

function divide {
	local var1=$1
	local var2=$2
	if [ $var2 -ne 0 ];then
		local quotient=$(echo "scale=2;$var1/$var2" | bc)
		local remainder=$(echo "$var1%$var2" | bc)
		echo "Quotient: $quotient"
		echo "Remainder: $remainder"
	else
		echo "ERROR: trying to divide by zero"
	fi
}

result=$(divide $1 $2)
echo "Result is: $result"

