#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    array = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        #check regex pattern in eual to emailID if yes append in array
        if re.search(".+@gmail\.com$", emailID):
            array.append(firstName)
    array.sort()

    for name in array:
        print(name)
