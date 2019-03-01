def swap_case(s):
    return ''.join([j.lower() if j.isupper() else j.upper() for j in s])

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
