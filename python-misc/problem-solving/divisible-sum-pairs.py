#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    combs = list(itertools.combinations(ar, 2))
    filtered = list(filter(lambda x: (x[0]+x[1])%k==0, combs))
    return len(filtered)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
