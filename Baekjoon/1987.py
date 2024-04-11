# https://www.acmicpc.net/problem/1987

r, c = map(int, input().strip().split())
graph = [list(input().strip()) for _ in range(r)]
visited = set()
max_count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    global max_count
    max_count = max(max_count, count)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in visited:
            visited.add(graph[nx][ny])
            dfs(nx, ny, count + 1)
            # 백트래킹: 이전 상태로 되돌림
            visited.remove(graph[nx][ny])

# 시작 지점 방문 처리
visited.add(graph[0][0])
dfs(0, 0, 1)

print(max_count)
