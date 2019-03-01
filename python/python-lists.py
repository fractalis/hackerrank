# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())

    lst = []

    for i in range(0, N):
        command_list = list(map(str, input().split()))

        command = command_list[0]

        if command == "print":
            print(lst)
        elif command == "insert":
            idx = int(command_list[1])
            val = int(command_list[2])
            lst.insert(idx, val)
        elif command == "append":
            val = int(command_list[1])
            lst.append(val)
        elif command == "reverse":
            lst = lst[::-1]
        elif command == "pop":
            lst = lst[:-1]
        elif command == "sort":
            lst = sorted(lst)
        elif command == "remove":
            val = int(command_list[1])
            lst.remove(val)

