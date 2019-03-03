# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    strs = []
    for i in range(0, len(string), k):
        strs.append(string[i:i+k])
    for x in strs:
        strDict = {}
        u = ""
        for c in x:
            if c not in strDict:
                u += c
                strDict[c] = c
        print(u)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
