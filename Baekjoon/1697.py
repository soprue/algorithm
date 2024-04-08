# https://www.acmicpc.net/problem/1697

from collections import deque

n, k = map(int, input().split())

visited = [-1] * 100001

def bfs():
    queue = deque([n])  # 시작 위치를 큐에 추가
    visited[n] = 0  # 시작 위치의 방문 시간을 0으로 설정

    while queue:
        x = queue.popleft() # 현재 위치

        # 동생을 찾았다면 종료
        if x == k: return visited[x]

        # 현재 위치에서 이동할 수 있는 3가지 경우를 탐색
        for next in (x - 1, x + 1, x * 2):
            # 범위 내에 있고 아직 방문하지 않은 위치라면
            if 0 <= next <= 100000 and visited[next] == -1:
                visited[next] = visited[x] + 1  # 이동 시간 업데이트
                queue.append(next)  # 다음 위치를 큐에 추가

print(bfs())
