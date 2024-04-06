# https://www.acmicpc.net/problem/2178

import sys
from collections import deque

input = sys.stdin.readline

# 미로의 크기 입력 받기
n, m = map(int, input().split())
# 미로 정보 입력 받기 (2차원 리스트)
maze = [list(map(int, list(input().strip()))) for _ in range(n)]

# 상하좌우 이동을 위한 방향 벡터 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 이동할 수 없는 칸인 경우 무시
            if maze[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1  # 이전 칸의 거리 +1을 현재 칸에 기록
                queue.append((nx, ny))  # 다음 위치를 큐에 삽입

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return maze[n-1][m-1]

print(BFS(0, 0))
