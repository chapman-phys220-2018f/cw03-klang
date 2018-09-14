#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Fibonacci Sequence Generator
# Trevor Kling
# 002270716
# kling109@mail.chapman.edu
# 9/11/2018
# CPSC 220

import sys


"""
 Returns a list of fibonacci numbers, up to and includign the supplied index.  The for loop iterates through the full range given,
and the results are appended to a temporary list.  Additionally, the function checks if the input was valid.  If not, a value error is thrown.
"""

def fibonacci(n):
    try:
        if int(n) >= 1:
            fibs = []
            currentNum = 1
            prevNum = 0
            temp = 0
            for i in range(0, int(n)):
                temp = currentNum
                currentNum = currentNum + prevNum
                prevNum = temp
                fibs.append(temp)
            return fibs
        else:
            print("That is not a valid input.")
    except ValueError:
        print("The input to this function must be an integer.")

"""
Runs the fibonacci function with an input from the command line.  If there are an incorrect number of arguments provided, an error message is displayed.
"""

def main(argv):
    if len(argv) == 2:
        print(fibonacci(argv[1]))
    else:
        print("That is not a valid number of inputs.  Input an integer as an argument.")

if __name__ == "__main__":
    main(sys.argv)

