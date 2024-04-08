# https://www.acmicpc.net/problem/24479

import sys

# 재귀 깊이 제한을 설정 (기본값보다 큰 문제를 해결하기 위함)
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m, r = map(int, input().split())

# 그래프를 저장할 딕셔너리 초기화 (무방향 그래프이므로 양쪽 방향 모두 저장)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visited = [0] * (n +1)  # 저장값
counter = 1

def dfs(start):
    global counter
    visited[start] = counter

    for next in graph[start]:  # 인접 정점을 오름차순으로 방문
        if visited[next] == 0:  # 아직 방문하지 않은 인접 정점에 대해
            counter += 1
            dfs(next)

dfs(r)

# 방문 순서 출력
for i in range(1, n+1):
    print(visited[i])
