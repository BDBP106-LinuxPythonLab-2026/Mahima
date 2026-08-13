#!/bin/bash
echo $HOME

divoutput=$(bc << EOF
scale=4
23934/44343
EOF
)
echo "the output for 23934/44343 is: $divoutput"

lsoutput=$(ls /home/ibab | grep "D")
echo "The files that start with 'D' are :$lsoutput"

grepoutput=$(cat /etc/passwd | grep -i ibab)
echo "The files with username are :$grepoutput"



