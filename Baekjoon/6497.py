# https://www.acmicpc.net/problem/6497

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

while True:
    # m: 집의 수, n: 길의 수
    m, n = map(int, input().strip().split())
    if m == 0 and n == 0: break

    total_cost = 0  # 모든 길을 켜는 데 필요한 총 비용
    mst_cost = 0

    edges = []
    for _ in range(n):
        x, y, z = map(int, input().strip().split())
        edges.append((z, x, y))
        total_cost += z
    edges.sort()

    parent = [i for i in range(m)]

    for cost, a, b in edges:
        if find(a) != find(b):
            union(a, b)
            mst_cost += cost

    # 절약할 수 있는 최대 비용 계산
    print(total_cost - mst_cost)
