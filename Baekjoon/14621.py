# https://www.acmicpc.net/problem/14621

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

# N: 학교의 수, M: 학교를 연결하는 도로의 수
N, M = map(int, input().strip().split())
types = input().strip().split()

edges = []
for _ in range(M):
    u, v, d = map(int, input().split())
    if types[u-1] != types[v-1]:  # 서로 다른 유형의 학교만 연결
        edges.append((d, u-1, v-1))
edges.sort()

parent = [i for i in range(N)]

result = 0
count = 0
for d, u, v in edges:
    if find(parent, u) != find(parent, v):
        union(parent, u, v)
        result += d
        count += 1
        if count == N-1:  # N-1개의 도로가 선택되면 모든 학교가 연결된 것
            break

if count == N-1:
    print(result)
else:
    print(-1)
