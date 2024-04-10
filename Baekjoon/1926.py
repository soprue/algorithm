# https://www.acmicpc.net/problem/1926

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().strip().split())
paper = [list(map(int, input().strip().split())) for _ in range(n)]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0
    
    # 현재 노드를 아직 방문하지 않았다면 방문 처리 후 현재 칸 넓이에 포함
    if paper[x][y] == 1:
        paper[x][y] = 0
        size = 1
        # 상하좌우로 연결되어 있는 그림 찾기
        size += dfs(x - 1, y)
        size += dfs(x + 1, y)
        size += dfs(x, y - 1)
        size += dfs(x, y + 1)
        return size

    return 0


count = 0
max_size = 0
for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            count += 1
            max_size = max(max_size, dfs(i, j))

print(count)
print(max_size)
