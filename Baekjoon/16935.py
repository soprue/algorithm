# https://www.acmicpc.net/problem/16935

import sys

# 상하 반전
def calc1(matrix):
    return matrix[::-1]

# 좌우 반전
def calc2(matrix):
    return [row[::-1] for row in matrix]

# 오른쪽 90도 회전
def calc3(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

# 왼쪽 90도 회전
def calc4(matrix):
    return [list(row) for row in zip(*matrix)][::-1]

# 1번 그룹의 부분 배열을 2번 그룹 위치로, 2번을 3번으로, 3번을 4번으로, 4번을 1번으로 이동
def calc5(matrix):
    N, M = len(matrix), len(matrix[0])
    temp = [[0] * M for _ in range(N)]
    for i in range(N // 2):
        for j in range(M // 2):
            temp[i][j+M // 2] = matrix[i][j]  # 1 -> 2
            temp[i+N // 2][j+M // 2] = matrix[i][j+M // 2]  # 2 -> 3
            temp[i+N // 2][j] = matrix[i+N // 2][j+M // 2]  # 3 -> 4
            temp[i][j] = matrix[i+N // 2][j]  # 4 -> 1
    return temp

# 1번 그룹의 부분 배열을 4번 그룹 위치로, 4번을 3번으로, 3번을 2번으로, 2번을 1번으로 이동
def calc6(matrix):
    N, M = len(matrix), len(matrix[0])
    temp = [[0] * M for _ in range(N)]
    for i in range(N // 2):
        for j in range(M // 2):
            temp[i+N//2][j] = matrix[i][j]  # 1 -> 4
            temp[i][j] = matrix[i][j+M//2]  # 2 -> 1
            temp[i][j+M//2] = matrix[i+N//2][j+M//2]  # 3 -> 2
            temp[i+N//2][j+M//2] = matrix[i+N//2][j]  # 4 -> 3
    return temp

N, M, _ = map(int, sys.stdin.readline().strip().split())

matrix = []
for _ in range(N):
    matrix.append(list(sys.stdin.readline().split()))

operations = list(map(int, sys.stdin.readline().split()))
 
for operation in operations:
    if operation == 1:
        matrix = calc1(matrix)
    elif operation == 2:
        matrix = calc2(matrix)
    elif operation == 3:
        matrix = calc3(matrix)
    elif operation == 4:
        matrix = calc4(matrix)
    elif operation == 5:
        matrix = calc5(matrix)
    else:
        matrix = calc6(matrix)

for i in matrix:
    print(*i)
