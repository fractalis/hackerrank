#!/bin/python3

N = int(input())

if N%2==1:
    print("Weird")
elif N>=2 and N<6:
    print("Not Weird")
elif N>=6 and N<21:
    print("Weird")
else:
    print("Not Weird")
