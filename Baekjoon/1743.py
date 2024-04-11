# https://www.acmicpc.net/problem/1743

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    # 상하좌우 이동을 위한 방향 벡터 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = True
    queue = deque([(x, y)])
    count = 1 # 현재 음식물 크기

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 위치가 범위 내에 있고, 방문하지 않은 음식물 쓰레기인 경우
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                count += 1 # 연결된 음식물 쓰레기 개수 증가
    
    return count

# n: 세로 길이, m: 가로 길이, k: 음식물 쓰레기 개수
n, m, k = map(int, input().strip().split())
graph = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().strip().split())
    graph[r - 1][c - 1] = 1

max_size = 0 # 가장 큰 음식물 쓰레기 크기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            max_size = max(max_size, bfs(i, j))  # 가장 큰 크기 갱신

print(max_size)
