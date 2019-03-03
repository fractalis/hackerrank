#!/bin/python3

# https://www.hackerrank.com/challenges/bon-appetit/problem

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    itms = bill[:k] + bill[k+1:]
    billTotal = sum(itms)/2
    if billTotal == b:
        print("Bon Appetit")
    else:
        print(int(b-billTotal))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

