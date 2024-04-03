# https://www.acmicpc.net/problem/1874

import sys

def stack_sequence(n, sequence):
    stack, result, count = [], [], 1
    for number in sequence:
        while count <= number:
            stack.append(count)
            result.append("+")
            count += 1
        if stack[-1] == number:
            stack.pop()
            result.append("-")
        else:
            return ["NO"]
    return result


N = int(sys.stdin.readline().strip())
num = [int(sys.stdin.readline().strip()) for _ in range(N)]

for operation in stack_sequence(N, num):
    print(operation)
