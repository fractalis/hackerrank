#!/bin/python3

#import math
import os
#import random
#import re
#import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    colors = set()
    matches = 0

    for s in ar:
        if not s in colors:
            colors.add(s)
        else:
            matches += 1
            colors.remove(s)
    return matches


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

