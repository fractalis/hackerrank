#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0]*(n)

    for query in queries:
        (a,b,c) = query
        arr[a-1] += c
        try:
            arr[b] -= c
        except:
            pass

    slope = 0
    for i in range(len(arr)):
        slope += arr[i]
        arr[i] = slope

    return max(arr)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open("out.txt",'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

