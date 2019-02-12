#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    flattened = [y for z in arr for y in z]

    len_row = len(arr[0])

    left_diag = flattened[::len_row+1]
    right_diag = flattened[len_row-1:-1:len_row-1]

    return abs(sum(left_diag)-sum(right_diag))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

