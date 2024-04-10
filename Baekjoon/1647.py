# https://www.acmicpc.net/problem/1647

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

N, M = map(int, input().strip().split())
edges =[]
for _ in range(M):
    a, b, cost = map(int, input().strip().split())
    edges.append((cost, a, b))
edges.sort()

parent = [i for i in range(N + 1)]

# 최소 스패닝 트리를 찾으면서 가장 비용이 큰 간선 기록
max_cost = 0
total_cost = 0
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total_cost += cost
        max_cost = max(max_cost, cost)
    
# 두 개의 분리된 마을로 만들기 위해 가장 비용이 큰 간선을 제거
# 최소 스패닝 트리(MST) 내에서 가장 비용이 큰 간선을 제거하는 이유
# -> 전체 그래프를 두 개의 분리된 마을(서브그래프)로 나누면서 그 사이의 연결 비용(유지비)을 최소화하기 위함
print(total_cost - max_cost)
