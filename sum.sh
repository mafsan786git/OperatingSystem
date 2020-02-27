#!/bin/bash

echo "Enter size n"
read n
sum=0
echo "Enter number to add"
for ((i=1;i<=n;i++))
do
  #sum=$((sum+i))
  read num
  sum=$(expr "$sum" + "$num" )
done

echo "The sum of given number is $sum"

: ' 
Enter size n
2
10
20
The sum of given number is 30

Enter size n
2
Enter number to add
10
10
The sum of given number is 20
'
