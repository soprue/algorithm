# https://www.acmicpc.net/problem/2638

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(N)]

# 외부 공기와 접촉하는 치즈를 찾기 위한 방향 벡터 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if grid[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    return visited

def melt_cheese(visited):
    new_cheese = []
    
    for x in range(N):
        for y in range(M):
            if grid[x][y] == 1:
                # 공기와 접촉하는 면의 수 계산
                count = 0
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if visited[nx][ny]:
                        count += 1
                # 2면 이상 접촉한 경우 녹음
                if count >= 2:
                    new_cheese.append((x, y))

    # 녹은 치즈 위치를 업데이트
    for x, y in new_cheese:
        grid[x][y] = 0

    return len(new_cheese)
 
time = 0
while True:
    visited = bfs()  # 외부 공기를 파악
    if melt_cheese(visited) == 0:
        break
    time += 1

print(time)
