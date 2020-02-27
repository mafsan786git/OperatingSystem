#!/bin/bash

echo "Enter number of series of fibbonacci"
read n
a=0
b=1
echo -n "$a $b "

for ((i=2;i<n;i++))
do
	temp=$((a+b))
	echo -n "$temp\b "
	a=$b
	b=$temp
done
echo ""

: '
Enter number of series of fibbonacci
8
0 1 1 2 3 5 8 13 
Enter number of series of fibbonacci
10
0 1 1 2 3 5 8 13 21 34'
