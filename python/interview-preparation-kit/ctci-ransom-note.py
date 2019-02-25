#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    m_dict = defaultdict(lambda: 0)

    for x in magazine:
        m_dict[x] += 1
    canMakeNote = True
    for x in note:
        if x in m_dict.keys() and m_dict[x] > 0:
            m_dict[x] -= 1
            continue
        else:
            canMakeNote = False
            break

    if canMakeNote: print("Yes")
    else: print("No")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

