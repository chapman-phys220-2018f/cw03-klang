#!/bin/bash

# Fibonacci Number Generator
# Trevor Kling
# PHYS 220
# 8/30/18

# Indexing begins at 0

nextNum=1
currentNum=1
previousNum=0
index=0

# Takes an input from the command line of a fibonacci number's index, then prints the corresponding number.

if [ $# == 0 ]
then
	echo "There was no number given.  Please input an integer when running this program."
	exit 1
elif [ $1 -lt 0 ]
then
	echo "Please input an integer greater than or equal to 0."
	exit 1
else
	until [ $index -eq $1 ]
	do
		echo -n "$currentNum"" "
		let nextNum=currentNum+previousNum
		let previousNum=currentNum
		let currentNum=nextNum
		let index+=1
	done
fi

echo

exit 0
