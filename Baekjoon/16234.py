import sys
from collections import deque 

input = sys.stdin.readline

N, L, R = map(int, input().strip().split())

countries = [list(map(int, input().strip().split())) for _ in range(N)]

days = 0
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while True:
    # 오늘 국경이 한 군데라도 열릴 수 있는지 '빠른 예비 점검'
    any_open = False
    for i in range(N):
        row = countries[i]
        for j in range(N):
            cur = row[j]
            # 오른쪽, 아래만 보면 중복 체크 안 함
            if j + 1 < N:
                diff = cur - row[j+1]
                if diff < 0: diff = -diff
                if L <= diff <= R:
                    any_open = True
                    break
            if i + 1 < N:
                diff = cur - countries[i+1][j]
                if diff < 0: diff = -diff
                if L <= diff <= R:
                    any_open = True
                    break
        if any_open:
            break
    if not any_open:
        break  # 오늘은 어떤 연합도 없음 → 종료
    
    # 연합 찾기
    visited = [[False] * N for _ in range(N)]
    moved = False
    
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            
            # BFS로 (i, j)에서 시작하는 '연합' 찾기
            q = deque()
            q.append((i, j))
            visited[i][j] = True
            
            cells = [(i, j)] # 연합에 속한 칸들
            total = countries[i][j] # 연합 인구 합
            count = 1 # 연합 칸 수
            
            while q:
                x, y = q.popleft()
                
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                        diff = abs(countries[x][y] - countries[nx][ny])
                        
                        if L <= diff <= R:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            cells.append((nx, ny))
                            total += countries[nx][ny]
                            count += 1
                            
            # 연합 크기가 2 이상이면 인구 재분배
            if count > 1:
                new_pop = total // count
                for x, y in cells:
                    countries[x][y] = new_pop
                moved = True
    
    days += 1
    
print(days)
