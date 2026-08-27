#question2
#i
awk ' $2<25 { print $0 } ' lab13awk.txt
#ii
awk ' $3=="Physics" { print $0 } ' lab13awk.txt
#iii
awk '{ print $1,",",$2,",",$3 }' lab13awk.txt > data2.csv
