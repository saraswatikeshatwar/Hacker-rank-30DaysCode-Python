#!/bin/python3

import sys


S = input().strip()
try:
    #int function convert string to integer
    print(int(S))
except:
    print('Bad String')
