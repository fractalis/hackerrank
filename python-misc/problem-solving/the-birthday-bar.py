#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the birthday function below.
def birthday(s, d, m):
    arr = []
    for i,y in enumerate(s):
        group = []
        for j in range(0,m):
            if i+j < len(s):
                group.append(s[i+j])
        if len(group) == m:
            arr.append(group)
    mapped = list(map(sum,arr))
    return mapped.count(d)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

