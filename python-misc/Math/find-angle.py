import math

if __name__ == "__main__":
    ab = int(input())
    bc = int(input())

    print("{0}".format(round(math.degrees(math.atan2(ab,bc)))))
