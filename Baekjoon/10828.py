# https://www.acmicpc.net/problem/10828

import sys

N = int(sys.stdin.readline().strip())
stack = []

for _ in range(N):
    command = sys.stdin.readline().strip()

    if command.startswith('push'):
        _, x = command.split()
        stack.append(int(x))
    elif command == "pop":
        print(stack.pop() if stack else -1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        print(0 if stack else 1)
    elif command == "top":
        print(stack[-1] if stack else -1)
