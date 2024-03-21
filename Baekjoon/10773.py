# https://www.acmicpc.net/problem/10773

import sys

K = int(sys.stdin.readline().strip()) 
stack = []

for _ in range(K):
    number = int(sys.stdin.readline().strip())
    if number == 0:
        stack.pop() 
    else:
        stack.append(number)

result = sum(stack)
print(result)
