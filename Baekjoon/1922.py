# https://www.acmicpc.net/problem/1922

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

N = int(input())
M = int(input())

edges = []
for _ in range(M):
    a, b, cost = map(int, input().strip().split())
    edges.append((cost, a, b))
edges.sort()

parent = [i for i in range(N + 1)]

result = 0
for edge in edges:
    cost, a, b = edge
    if(find(parent, a) != find(parent, b)):
        union(parent, a, b)
        result += cost
print(result)
