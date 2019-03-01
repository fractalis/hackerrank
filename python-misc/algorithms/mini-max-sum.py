#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_a = arr[0]
    max_a = arr[0]
    sum_a = 0

    for x in arr:
        if x < min_a:
            min_a = x
        if x > max_a:
            max_a = x
        sum_a += x

    print("{0} {1}".format(sum_a-max_a, sum_a-min_a))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

