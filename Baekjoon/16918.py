import sys

input = sys.stdin.readline

R, C, N = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def explode(G):
  R, C = len(G), len(G[0])

  # 폭발해서 빈칸으로 바뀔 자리 찾기
  temp_grid = [[False] * C for _ in range(R)]
  for i in range(R):
    for j in range(C):
      if G[i][j] == 'O':
        temp_grid[i][j] = True
        for dx, dy in dirs:
          ni, nj = i + dx, j + dy
          if 0 <= ni < R and 0 <= nj < C:
            temp_grid[ni][nj] = True

  # 다음 격자
  next_grid = [['O'] * C for _ in range(R)]
  for i in range(R):
    for j in range(C):
      if temp_grid[i][j]:
        next_grid[i][j] = '.'

  return next_grid

def print_grid(arr):
  for row in arr:
    print(''.join(row))

if N == 1:
  print_grid(grid)
elif N % 2 == 0:
  for _ in range(R):
    print('O' * C)
else:
  once = explode(grid)
  if N % 4 == 3:
    print_grid(once)
  else:
    twice = explode(once)
    print_grid(twice)
