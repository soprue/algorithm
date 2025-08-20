import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().strip().split())

MAX = 100000
dist = [-1] * (MAX + 1) # 방문 여부 확인 + 최소 시간 저장
dist[N] = 0

queue = deque()
queue.append(N)

while queue:
    x = queue.popleft()

    if x == K:
        print(dist[x])
        break

    nx = x * 2
    if 0 <= nx <= MAX and dist[nx] == -1:
        dist[nx] = dist[x]
        queue.appendleft(nx) # 0초 = 앞쪽에 넣기 

    for nx in (x - 1, x + 1):
        if 0 <= nx <= MAX and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            queue.append(nx) # 1초 = 뒤쪽에 넣기
