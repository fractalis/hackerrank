#!/bin/python3

import os
import sys
import functools

#
# Complete the getTotalX function below.
def gcd(a,b):
    if (b == 0):
        return a
    return gcd(b, a%b)

def lcm(a,b):
    return (a*b)/gcd(a,b)

def getTotalX(a, b):
    lcm_a = functools.reduce(lcm, a)
    gcd_b = functools.reduce(gcd, b)

    cnt = 0
    multiple = 1
    while True:
        if gcd_b%(lcm_a*multiple)==0:
            cnt+=1
        if lcm_a*multiple >= gcd_b:
            break
        multiple += 1
    return cnt

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()

