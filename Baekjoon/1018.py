# https://www.acmicpc.net/problem/1018

import sys

M, N = map(int, sys.stdin.readline().strip().split())
board = [sys.stdin.readline().strip() for _ in range(M)]

color = {0 : "B", 1 : "W"}
count_list = []

for x_start in range(M - 7):
    for y_start in range(N - 7):
        paint_w, paint_b = 0, 0

        for x in range(x_start, x_start + 8):
            for y in range(y_start, y_start + 8):
                # 검은색 시작일 때 틀린 경우
                if board[x][y] != color[(x + y) % 2]:
                    paint_b += 1
                # 흰색 시작일 때 틀린 경우
                else:
                    paint_w += 1
        
        paint = min(paint_b, paint_w)
        count_list.append(paint)

print(min(count_list))
