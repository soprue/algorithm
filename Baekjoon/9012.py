# https://www.acmicpc.net/problem/9012

import sys

T = int(sys.stdin.readline().strip())

def isVPS(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

for _ in range(T):
    print(isVPS(sys.stdin.readline().strip()))
