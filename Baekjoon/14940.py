import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]

dist = [[-1] * M for _ in range(N)]
  
sx = sy = -1 # 시작점(2) 위치 
for i in range(N):
  for j in range(M):
    if arr[i][j] == 0:
      dist[i][j] = 0
    elif arr[i][j] == 2:
      sx, sy = i, j

# bfs
q = deque()
q.append((sx, sy))
dist[sx][sy] = 0

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while q:
  x, y = q.popleft()
   
  for dx, dy in dirs:
    nx, ny = x + dx, y + dy

    if 0 <= nx < N and 0 <= ny < M:
      if arr[nx][ny] != 0 and dist[nx][ny] == -1:
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx, ny))

for i in range(N):
  print(*dist[i])
