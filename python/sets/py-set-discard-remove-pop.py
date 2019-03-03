n = int(input())
s = set(map(int, input().split()))
ops = int(input())

for i in range(0, ops):
    command = str(input())
    cmds = command.split(" ")
    if cmds[0] == "pop":
        s.pop()
    if cmds[0] == "discard":
        s.discard(int(cmds[1]))
    if cmds[0] == "remove":
        s.discard(int(cmds[1]))
print(sum(list(s)))
