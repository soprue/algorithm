# https://www.acmicpc.net/problem/2667

n = int(input().strip())
map = [list(map(int, list(input().strip()))) for _ in range(n)]

home = 0
visited = [[False] * n for _ in range(n)]

# 함수가 호출되면 해당 위치에서 시작하여 연결된 모든 집 탐색
def DFS(x, y):
    global home 

    # 지도의 범위를 벗어난 경우, 집이 없거나 이미 방문한 경우 False 반환
    if x < 0 or x >= n or y < 0 or y >= n or \
    visited[x][y] or map[x][y] == 0: 
        return False
    
    if map[x][y] == 1 and not visited[x][y]:
        home += 1
        visited[x][y] = True
        DFS(x - 1, y)
        DFS(x + 1, y)
        DFS(x, y - 1)
        DFS(x, y + 1)
        return True  # 연결된 집들을 모두 방문 처리했으므로 True 반환

# 각 단지별 집의 수를 저장할 리스트
counts = []

# 모든 위치를 순회하며 DFS 실행
for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            counts.append(home) # 리스트에 집의 수 출력
            home = 0 # 한 단지에 있는 집의 수를 다시 0으로 초기화

# 단지별 집의 수 오름차순 정렬
counts.sort()

print(len(counts))
for count in counts:
    print(count)
