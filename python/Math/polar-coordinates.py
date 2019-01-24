import cmath

if __name__ == '__main__':
    x = input()
    print(abs(complex(x)))
    print(cmath.phase(complex(x)))
