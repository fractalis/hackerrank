import math
import os
import random
import re
import sys

from collections import defaultdict
from itertools import combinations

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
	substrings = [s[i:j+1] for i in range(0,len(s)) for j in range(i,len(s))]
	sorted_substrings = [''.join(sorted(x)) for x in substrings]

	substring_dict = defaultdict(lambda: [])
	total = 0

	for x in sorted_substrings:
		substring_dict[x].append(x)
	for x in substring_dict.keys():
		if len(substring_dict[x]) > 1:
			total += len(list(combinations(substring_dict[x],2)))
	return total



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

