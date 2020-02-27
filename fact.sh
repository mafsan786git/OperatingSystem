#!/bin/bash

echo "Enter number to find factorial"
read n
fact=1
if [ "$n" -lt "2" ]
then
	echo $fact
else
	for ((i=1;i<=n;i++))
	do
		fact=$((fact*i))
	done
	echo "factorial of $n is $fact"
fi

: '
Enter number to find factorial
6
factorial of 6 is 720
Enter number to find factorial
5
fcatorial of 5 is 120
Enter number to find factorial
0
1
'
