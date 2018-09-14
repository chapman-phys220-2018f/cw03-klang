#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Fibonacci Sequence Generator
# Trevor Kling
# 002270716
# kling109@mail.chapman.edu
# 9/11/2018
# CPSC 220

import sys
import sequences

"""
Takes a command line argument, then prints the fibonacci number at the given index.  If an invalid number of arguments is given, an error message is displayed.
"""

def main(argv):
    if len(argv) == 2:
        valueList = sequences.fibonacci(argv[1])
        print(valueList[len(valueList)-1])
    else:
        print("That is not a valid number of inputs.  Input an integer as an argument.")

if __name__ == "__main__":
    main(sys.argv)
