# https://www.acmicpc.net/problem/5014

from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [False] * (F + 1)

def bfs():
    # 큐 초기화, (현재 층, 버튼 누른 횟수)
    queue = deque([(S, 0)])
    visited[S] = True

    while queue:
        current, count = queue.popleft()
        
        # 목표 층에 도달한 경우
        if current == G:
            return count
        
        # U 버튼을 눌러 이동
        if current + U <= F and not visited[current + U]:
            visited[current + U] = True
            queue.append((current + U, count + 1))
            
        # D 버튼을 눌러 이동
        if current - D >= 1 and not visited[current - D]:
            visited[current - D] = True
            queue.append((current - D, count + 1))
    
    # 목표 층에 도달할 수 없는 경우
    return "use the stairs"

print(bfs())
