# https://www.acmicpc.net/problem/10423

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

# N: 도시의 개수, M: 설치 가능한 케이블 수, K: 발전소 개수
N, M, K = map(int, input().strip().split())
# 발전소가 설치된 도시 번호
power_plants = list(map(int, input().strip().split()))

edges = []
for _ in range(M):
    u, v, w = map(int, input().strip().split())
    edges.append((w, u, v))
edges.sort()

# 초기화: 모든 발전소를 같은 그룹에 속하도록 설정
# 모든 발전소를 '0'이라는 수퍼노드에 연결
parent = [i for i in range(N + 1)]
for plant in power_plants:
    parent[plant] = 0 

total_cost = 0
for cost, u, v in edges:
    if find(parent, u) != find(parent, v):
        union(parent, u, v)
        total_cost += cost


connected = True
root = find(parent, 1)
for i in range(1, N+1):
    if find(parent, i) != root:
        connected = False
        break

# 모든 도시가 연결되었는지 확인
if connected:
    print(total_cost)
else:
    print(-1)
