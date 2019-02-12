#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time = list(map(int, s[:-2].split(":")))
    am_or_pm = s[-2::1]

    if am_or_pm == "PM" and time[0] != 12:
        time[0] += 12
    elif am_or_pm == "AM" and time[0] == 12:
        time[0] = 0

    return "{0:02d}:{1:02d}:{2:02d}".format(time[0],time[1],time[2])


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

