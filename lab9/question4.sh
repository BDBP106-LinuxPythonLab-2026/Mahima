#!/bin/bash

echo $0
name=$1
age=$2

echo 'The first argument is',$1
echo 'The second argument is',$2

echo 'The numbers of arguments passed to the script:'$#
echo 'The array/list of rguments passed to the script:'$@

# We can store the arguments in an array be enclosing $@ within ()
listofargs=($@)
# Recall elements like any other array
echo ${listofargs[2]}
