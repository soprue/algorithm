# https://www.acmicpc.net/problem/16398

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


n = int(input())  # 행성의 수
arr = [list(map(int, input().split())) for _ in range(n)]  # 각 행성간의 플로우 관리 비용

edges = []  # 행성 간선 정보
# arr이 대각선(↘)을 기준으로 삼각형이 대칭이니
# 한쪽의 삼각형 부분 데이터만 간선 정보로 넣어주면 됨
for i in range(1, n):
    for j in range(i):
        edges.append((arr[i][j], i, j))
edges.sort()  # 행성 간선 정보를 최소 비용 순으로 정렬

result = 0
parent = [i for i in range(n)]
for cost, a, b in edges:
    if find(parent, a) != find(parent, b): 
        union(parent, a, b)
        result += cost

print(result)
