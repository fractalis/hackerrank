#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
	swaps = 0
	for i in range(len(a)):
		for j in range(len(a)-1):
			if a[j]  > a[j+1]:
				swaps += 1
				a[j],a[j+1] = a[j+1],a[j]
	print("Array is sorted in {0} swaps.".format(swaps))
	print("First Element: {0}".format(a[0]))
	print("Last Element: {0}".format(a[-1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

