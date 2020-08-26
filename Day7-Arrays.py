#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    array = arr[::-1]
    #map fuct iterates sequence
    #join combines string and array
    print(" ".join(map(str,array)))
