# https://www.acmicpc.net/problem/2445

import sys

N = int(sys.stdin.readline().strip())

for i in range(1, N + 1):
    left_stars = "*" * i
    middle_space = " " * 2 * (N - i)
    right_stars = "*" * i
    print(left_stars + middle_space + right_stars)

for j in range(1, N + 1):
    left_stars = "*" * (N - j)
    middle_space = " " * 2 * j
    right_stars = "*" * (N - j)
    print(left_stars + middle_space + right_stars)
