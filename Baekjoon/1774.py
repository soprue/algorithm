# https://www.acmicpc.net/problem/1774

from math import sqrt
import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def distance(x, y):
    return sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

N, M = map(int, input().strip().split())
coordinates = [tuple(map(int, input().split())) for _ in range(N)]

edges = []
# 모든 우주신 간 가능한 통로와 그 거리 계산
for i in range(N):
    for j in range(i + 1, N):
        dist = distance(coordinates[i], coordinates[j])
        edges.append((dist, i, j))
edges.sort()

parent = [i for i in range(N)]

# 이미 연결된 통로 처리
for _ in range(M):
    a, b = map(int, input().split())
    union(parent, a - 1, b - 1)

total_cost = 0
for cost, u, v in edges:
    if find(parent, u) != find(parent, v):
        union(parent, u, v)
        total_cost += cost

# 결과 출력
print(f"{total_cost:.2f}")
