# https://www.acmicpc.net/problem/2445

import sys

N = int(sys.stdin.readline().strip())

for i in range(1, N + 1):
    star = '*' * i
    space = ' ' * (2 * (N - i))
    print(star + space + star)

for i in range(N - 1, 0, -1):
    star = '*' * i
    space = ' ' * (2 * (N - i))
    print(star + space + star)
    
