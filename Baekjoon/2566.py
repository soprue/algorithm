# https://www.acmicpc.net/problem/2566

import sys

table = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
MAX = 0
MAX_ROW, MAX_COL = 0, 0

for row in range(9):
    for col in range(9):
        if MAX <= table[row][col]:
            MAX = table[row][col]
            MAX_ROW = row + 1
            MAX_COL = col + 1

print(MAX)
print(MAX_ROW, MAX_COL)
