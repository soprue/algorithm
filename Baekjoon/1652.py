# https://www.acmicpc.net/problem/1652

import sys

def findRow(row):
    flag = 0
    count = 0
    for val in row:
        if val == '.':
            flag += 1
            if flag == 2:
                count += 1
        else:
            flag = 0
    return count

def findCol(matrix):
    count = 0
    for i in range(len(matrix)):
        flag = 0
        for j in range(len(matrix)):
            if matrix[j][i] == '.':
                flag += 1
                if flag == 2:
                    count += 1
            else:
                flag = 0
    return count             

N = int(sys.stdin.readline().strip())

matrix = []
rowCount, colCount = 0, 0

for i in range(N):
    matrix.append(sys.stdin.readline().strip())

rowCount = sum(findRow(row) for row in matrix)
colCount = findCol(matrix)

print(rowCount, colCount)
