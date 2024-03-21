# https://www.acmicpc.net/problem/10807

import sys

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
v = int(sys.stdin.readline().strip())

count_v = numbers.count(v)

print(count_v)
