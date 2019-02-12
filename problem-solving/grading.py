#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
	final_grades = []

	for grade in grade:
		if grade < 38:
			final_grades.append(grade)
		elif grade%5 >= 3:
			final_grades.append(grade+(5-grade%5))
		else:
			final_grades.append(grade)
	return final_grades


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()

