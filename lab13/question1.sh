#question1
#i
sed -n '/and/p' lab13.sh
#ii
sed 's/language/lang/g' lab13.txt
#iii
sed '/is/d' lab13.txt
#iv
sed '=' lab13.txt | sed 'N;s/\n/ /'
#v
sed '1,2d' lab13.txt
#vi
sed -n '1~2p' lab13.txt
#vii
sed 's/Python/python/;s/language/lang/' lab13.txt
