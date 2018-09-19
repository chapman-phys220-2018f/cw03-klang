#!/bin/bash


# Fib runner
# Conner Carnahan
#

# runs the fibs algorythm for 1 to 10000

inum=$@

if [ $inum -le 0 ]; then
	echo "Type an integer greater than or equal to 1"
	exit 1
fi

if [ $inum -gt 10000 ]; then
	echo "Okay, but also type one less than 10,000"
	exit 1
fi

if [ -f fibs.csv.bak ]; then
	echo "A backup already exists, I'm gone"
	exit 0
fi

if [ -f fibs.csv ]; then
	mv fibs.csv fibs.csv.bak
	echo "A file has been backed up"
fi

for w in $(seq $inum); do echo -n $(./fib.py $w) "," >> fibs.csv; done

exit 0

