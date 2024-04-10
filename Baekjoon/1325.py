# https://www.acmicpc.net/problem/1325

from collections import deque
import sys
input = sys.stdin.readline

 # bfs를 통해 i번 컴퓨터를 해킹했을 때 해킹할 수 있는 컴퓨터의 수 계산
def bfs(start):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1

    return count

n, m = map(int, input().strip().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[b].append(a) # # b를 해킹하면 a도 해킹할 수 있다는 의미 -> b의 리스트에 a 추가

# result: 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 저장할 리스트
result = []
max_count = 0

for i in range(1, n + 1):
    c = bfs(i)
    if c > max_count:
        result = [i]
        max_count = c
    elif c == max_count:
        result.append(i)

print(*result)
