# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()

    print("True") if len(list(filter(str.isalnum, s))) > 0 else print("False")
    print("True") if len(list(filter(str.isalpha, s))) > 0 else print("False")
    print("True") if len(list(filter(str.isdigit, s))) > 0 else print("False")
    print("True") if len(list(filter(str.islower, s))) > 0 else print("False")
    print("True") if len(list(filter(str.isupper, s))) > 0 else print("False")
