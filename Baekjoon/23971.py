# https://www.acmicpc.net/problem/23971

import sys
from math import ceil

# H: 행, W: 열, N: 세로 거리두기, M: 가로 거리두기
H, W, N, M = map(int, sys.stdin.readline().split(" "))

rows = ceil(H / (N + 1))
cols = ceil(W / (M + 1))

print(rows * cols)
