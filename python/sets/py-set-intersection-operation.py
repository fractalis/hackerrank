n = int(input())
s1 = set(map(int, input().split()))
n = int(input())
s2 = set(map(int, input().split()))

s_i = s1.intersection(s2)

print(len(s_i))
