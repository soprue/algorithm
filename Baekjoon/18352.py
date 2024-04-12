# https://www.acmicpc.net/problem/18352

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    distance[start] = 0

    while queue:
        current = queue.popleft()

        for next in graph[current]:
            if distance[next] == -1: # 아직 방문하지 않은 노드
                distance[next] = distance[current] + 1
                queue.append(next)


# N: 도시의 개수, M: 도로의 개수, K: 최단 거리, X: 출발 도시의 번호
N, M, K, X = map(int, input().strip().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().strip().split())
    graph[A].append(B)

# 최단 거리 계산을 위한 초기화
distance = [-1] * (N + 1)

bfs(X)

found = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        found = True

if not found:
    print(-1)
