# https://www.acmicpc.net/problem/2606

import sys

input = sys.stdin.readline

# n: 컴퓨터의 수
# e: 연결 쌍의 수
n = int(input())
e = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def DFS(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

# 1번 컴퓨터부터 시작하여 DFS 실행
DFS(graph, 1, visited)
# 방문한 컴퓨터의 수를 출력(1번 컴퓨터는 제외해야 하므로 -1)
print(visited.count(True) - 1)
