# https://www.acmicpc.net/problem/1520

import sys
input = sys.stdin.readline

# M: 세로 크기, N: 가로 크기
M, N = map(int, input().strip().split())
map = [list(map(int, input().strip().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    # 도착 지점에 도착한 경우
    if x == M - 1 and y == N - 1: return 1

    # 이미 방문한 적 있는 지점인 경우 그 위치에서 출발하는 경우의 수를 리턴
    if dp[x][y] != -1: return dp[x][y]
    
    # 아직 계산되지 않은 경우
    dp[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and map[nx][ny] < map[x][y]:
            dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

print(dfs(0, 0))
