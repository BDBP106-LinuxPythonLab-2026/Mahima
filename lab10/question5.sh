#!/bin/bash

echo "score:"
read score

if [ "$score" -ge 90 ];then
	echo "A"
fi

if [ "$score" -ge 80 ] && [ "$score" -lt 90 ];then
	echo 'B'
fi

if [ "$score" -ge 70 ] && [ "$score" -lt 80 ];then
	echo 'C'
fi

if [ "$score" -lt 70 ];then
	echo 'Fail'
fi

