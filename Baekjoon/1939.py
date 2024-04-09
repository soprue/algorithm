# https://www.acmicpc.net/problem/1939

from collections import deque
import sys
input = sys.stdin.readline

# 섬의 개수 n, 다리 정보의 개수 m
n, m = map(int, input().split())

# 각 섬을 연결하는 다리 정보 저장
bridges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())  # a와 b를 연결하는 다리의 중량 제한 c
    bridges[a].append((b, c))
    bridges[b].append((a, c))

# 공장이 위치한 섬의 번호
factory_start, factory_end = map(int, input().split())

# 해당 중량으로 시작점에서 끝점까지 이동할 수 있는지 확인하는 함수
def BFS(c):
    visited = [False] * (n + 1)
    visited[factory_start] = True
    queue = deque([factory_start])

    while queue:
        current = queue.popleft()

        for next, weight in bridges[current]:
            if not visited[next] and weight >= c:
                visited[next] = True
                queue.append(next)

    return visited[factory_end]

# 이진 탐색을 통한 최대 중량 제한 찾기
left, right = 1, 1000000000
max_weight = 0

while left <= right:
    mid = (left + right) // 2

    if BFS(mid):  # mid 중량으로 이동이 가능하면 중량 늘림
        max_weight = mid
        left = mid + 1
    else:  # 이동이 불가능하면 중량을 줄임
        right = mid - 1

print(max_weight)
