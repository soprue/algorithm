# https://www.acmicpc.net/problem/11660

import sys
input = sys.stdin.readline

# N: 표의 크기, M: 합을 구해야 하는 횟수
N, M = map(int, input().strip().split())

#  N x N 표 데이터
arr = [[0] * (N + 1)]
for _ in range(N):
    row = [0] + list(map(int, input().split()))
    arr.append(row)

# 누적 합 배열을 계산
prefix = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        # 각 칸까지의 누적합을 계산
        # 현재 위치의 값 = 왼쪽의 누적합 + 위쪽의 누적합 - i-1열 j-1행의 누적합
        prefix[i][j] = arr[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

# 쿼리 처리
results = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    # 주어진 범위 (x1, y1) ~ (x2, y2)의 합을 누적 합 배열을 사용하여 계산
    result = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]
    results.append(result)

# 결과 출력
for result in results:
    print(result)
