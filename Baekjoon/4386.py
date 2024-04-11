# https://www.acmicpc.net/problem/4386

from math import sqrt

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

def distance(star1, star2):
    return sqrt((star1[0] - star2[0]) ** 2 + (star1[1] - star2[1]) ** 2)

n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
edges = []

# 모든 별들 사이의 거리 계산하여 간선 리스트 생성
for i in range(n):
    for j in range(i+1, n):
        edges.append((distance(stars[i], stars[j]), i, j))

# 간선을 거리에 따라 오름차순으로 정렬
edges.sort()

parent = [i for i in range(n)]
result = 0
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(f"{result:.2f}")
