#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    min_breaks, max_breaks = 0, 0
    min_s,max_s = scores[0],scores[0]

    for score in scores[1:]:
        if score < min_s:
            min_s = score
            min_breaks += 1
        if score > max_s:
            max_s = score
            max_breaks += 1
    return [max_breaks, min_breaks]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

