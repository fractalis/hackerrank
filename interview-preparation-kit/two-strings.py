#!/bin/python3

import os

# Complete the twoStrings function below.
def twoStrings(s1, s2):
	match = 'NO'
	lmap = {}
	for x in s1:
		lmap[x] = 1
	for x in s2:
		if x in lmap:
			match = 'YES'
	return match

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
