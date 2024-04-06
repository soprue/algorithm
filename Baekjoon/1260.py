# https://www.acmicpc.net/problem/1260

import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문해야 함
# -> 각 정점의 인접 리스트를 정렬
for adj_list in graph:
    adj_list.sort()

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

DFS(graph, v, visited)
print()

# BFS를 시작하기 전에 visited 배열을 재초기화
visited = [False] * (n + 1)
BFS(graph, v, visited)
