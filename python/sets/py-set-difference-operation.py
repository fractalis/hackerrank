n = int(input())
s1 = set(map(int, input().split()))
n = int(input())
s2 = set(map(int, input().split()))

s_d = s1.difference(s2)

print(len(s_d))
