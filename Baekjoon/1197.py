# https://www.acmicpc.net/problem/1197

# 크루스칼 알고리즘 구현 단계 
# 1. 모든 간선을 가중치에 따라 오름차순으로 정렬
# 2. 간선을 하나씩 확인하며, 현재 간선이 사이클을 발생시키지 않는 경우에만 선택
#    유니온-파인드 자료구조를 사용하여 두 정점이 이미 같은 트리에 속해 있는지(사이클을 형성하는지) 확인
# 3. 선택된 간선들의 가중치 합을 계산, 이 값이 최소 스패닝 트리의 가중치가 됨

import sys
input = sys.stdin.readline

# 유니온 파인드 함수 정의
def find(parent, x):
    # 재귀적으로 부모 노드를 찾아 반환함 (경로 압축 기법)
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    # 두 원소의 루트 노드를 찾음
    a = find(parent, a)
    b = find(parent, b)
    # 두 루트 노드 중 작은 것을 큰 것의 부모로 설정하여 두 트리를 합침
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())

edges = []
for _ in range(E):
    a, b, cost = map(int, input().strip().split())
    edges.append((cost, a, b))
# 간선을 비용 순으로 정렬
edges.sort()

# 유니온 파인드를 위한 부모 테이블 초기화
parent = [i for i in range(V + 1)]

# result: 최소 스패닝 트리의 가중치 합
result = 0
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우 (두 정점의 루트 노드가 다른 경우)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)
