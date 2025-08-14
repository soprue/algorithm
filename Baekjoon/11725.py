import sys

# DFS처럼 재귀 호출을 많이 쓰는 알고리즘에서 트리 깊이가 수만, 수십만이 될 수도 있는데, 파이썬은 기본 재귀 깊이가 약 1,000단계 정도로 제한되어 있음.
# sys.setrecursionlimit(10**6)이면 최대 100만 단계까지 재귀 허용. 이렇게 하면 깊은 트리나 그래프에서도 DFS 재귀가 끊기지 않음.
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input().strip())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
  a, b = map(int, input().strip().split())
  graph[a].append(b)
  graph[b].append(a)

parent = [0] * (N + 1)
visited = [False] * (N + 1)

def dfs(node):
  visited[node] = True
  for next in graph[node]:
    # 방문 안 했다면 처음 발견된 것이므로, 트리에서 node → next는 부모-자식 관계가 됨
    if not visited[next]:
      parent[next] = node
      dfs(next)
    
dfs(1)

for i in range(2, N + 1):
  print(parent[i])
