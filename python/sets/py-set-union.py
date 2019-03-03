n = int(input())
s1 = set(map(int, input().split()))
n = int(input())
s2 = set(map(int, input().split()))

s_u = s1.union(s2)

print(len(s_u))
