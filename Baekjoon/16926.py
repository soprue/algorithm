# https://www.acmicpc.net/problem/16926

import sys

def rotate_matrix(N, M, R, matrix):
    for layer in range(min(N, M) // 2):
        # 레이어의 시작점과 끝점
        start_row, start_col = layer, layer
        end_row, end_col = N - layer - 1, M - layer - 1
    
        # 현재 레이어의 원소들을 임시로 저장할 리스트
        temp = []
        
        # 상단 가로줄
        for col in range(start_col, end_col + 1):
            temp.append(matrix[start_row][col])
        # 우측 세로줄
        for row in range(start_row + 1, end_row + 1):
            temp.append(matrix[row][end_col])
        # 하단 가로줄
        for col in range(end_col - 1, start_col - 1, -1):
            temp.append(matrix[end_row][col])
        # 좌측 세로줄
        for row in range(end_row - 1, start_row, -1):
            temp.append(matrix[row][start_col])
        
        # R번 회전
        rotate_count = R % len(temp)
        temp = temp[rotate_count:] + temp[:rotate_count]
        
        # 회전된 원소들을 다시 배열에 배치
        temp_idx = 0
        for col in range(start_col, end_col + 1):
            matrix[start_row][col] = temp[temp_idx]
            temp_idx += 1
        for row in range(start_row + 1, end_row + 1):
            matrix[row][end_col] = temp[temp_idx]
            temp_idx += 1
        for col in range(end_col - 1, start_col - 1, -1):
            matrix[end_row][col] = temp[temp_idx]
            temp_idx += 1
        for row in range(end_row - 1, start_row, -1):
            matrix[row][start_col] = temp[temp_idx]
            temp_idx += 1

    return matrix

N, M, R = map(int, sys.stdin.readline().strip().split())

matrix = []

for _ in range(N):
    matrix.append(list(sys.stdin.readline().split()))

matrix = rotate_matrix(N, M, R, matrix)

for i in range(N):
    for j in range(M):
        print(matrix[i][j], end=' ')
    print()
