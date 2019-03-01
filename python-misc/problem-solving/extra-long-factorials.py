#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    total = 1
    while n > 1:
        total = total * n
        n = n - 1
    print(total)

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)

