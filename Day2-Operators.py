#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_Cost, tip_percent, tax_percent):
        tip = meal_Cost * tip_percent / 100
        tax = meal_Cost * tax_percent / 100
        totalCost = meal_Cost + tip + tax
        print(str(round(totalCost)) )  
if __name__ == '__main__':
    meal_Cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    solve(meal_Cost, tip_percent, tax_percent)
