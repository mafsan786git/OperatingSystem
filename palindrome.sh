#!/bin/bash

echo "Enter the string : "
read string

len=${#string}
#rev=$(echo $string | rev) this is also correct
for (( i=$len-1;i>=0;i-- ))
do
	reverse="$reverse${string:$i:1}"
done

if [ "$string" == "$rev" ]
then
	echo "$string is palindrome"
else
	echo "$string is not palindrome"
fi

: '
Enter the string : 
lol
lol is palindrome
Enter the string : 
afsan
afsan is not palindrome

'
