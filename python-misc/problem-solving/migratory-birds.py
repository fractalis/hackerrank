#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    a_dict = defaultdict(lambda: 0)
    l_dict = defaultdict(lambda: [])

    for x in arr:
        a_dict[x] += 1
    for k,v in a_dict.items():
        l_dict[v].append(k)

    return min(l_dict[max(l_dict.keys())])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

