# https://www.acmicpc.net/problem/16236

import heapq
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
    queue = deque([(start[0], start[1], 0)])  # 큐에는 (x, y, 시간)을 저장

    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True
    fishes = []  # 먹을 수 있는 물고기 리스트
    
    while queue:
        x, y, dist = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if grid[nx][ny] <= size:  # 이동 가능
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
                    if 0 < grid[nx][ny] < size:  # 먹을 수 있는 물고기
                        fishes.append((dist + 1, nx, ny))
    
    if fishes:
        fishes.sort()  # 거리, x, y 순으로 정렬
        return fishes[0]  # 가장 가까운 물고기 반환
    return None

N = int(input().strip())
grid = []
shark = None

for i in range(N):
    row = list(map(int, input().strip().split()))
    grid.append(row)
    for j in range(N):
        if row[j] == 9:
            shark = (i, j)
            grid[i][j] = 0  # 초기 상어 위치는 빈 칸으로 설정

size = 2 # 아기 상어의 크기
eat = 0
time = 0

while True:
    result = bfs(shark)
    if not result: break  # 먹을 수 있는 물고기가 없으면 종료

    dist, nx, ny = result
    time += dist  # 총 시간에 이동 시간 추가
    eat += 1

    if eat == size:  # 성장 조건 충족
        size += 1
        eat = 0

    grid[nx][ny] = 0  # 먹은 물고기 위치 초기화
    shark = (nx, ny)  # 상어 위치 업데이트

print(time)
