# https://www.acmicpc.net/problem/2468

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
max_height = max(map(max, area)) # 최대 물 높이

def bfs(x, y, h):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        # 네 방향, 범위 내, 미방문, 높이 > h 확인
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and area[nx][ny] > h:
                visited[nx][ny] = True
                queue.append((nx, ny))

max_safe_areas = 0

for h in range(max_height):
    visited = [[False] * n for _ in range(n)]

    # h 높이에 대해 잠기지 않는 영역 개수 리턴
    safe_areas = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and area[i][j] > h:
                bfs(i, j, h)
                safe_areas += 1

    max_safe_areas = max(max_safe_areas, safe_areas)

print(max_safe_areas)
