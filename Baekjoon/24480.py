# https://www.acmicpc.net/problem/24480

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) 

# N: 정점의 수, M: 간선의 수, R: 시작 정점
N, M, R = map(int, input().strip().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)
    
# 그래프의 각 인접 리스트를 내림차순으로 정렬
for edges in graph:
    edges.sort(reverse=True)
    

visited = [0] * (N + 1)
count = 1
def dfs(start):
    global count
    visited[start] = count
    
    for i in graph[start]:
        if visited[i] == 0:
            count += 1
            dfs(i)

dfs(R)
for val in visited[1:]:
    print(val)
