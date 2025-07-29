import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
garden = [list(map(int, input().split())) for _ in range(N)]

# 꽃 하나가 차지하는 상대 좌표
flower_offsets = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

# 가능한 중심 좌표: (1,1) ~ (N-2,N-2)
candidates = [(x, y) for x in range(1, N - 1) for y in range(1, N - 1)]

min_cost = float('inf')

# 중심 좌표 3개를 조합으로 고르기
for comb in combinations(candidates, 3):
    visited = set()
    total_cost = 0
    valid = True

    for x, y in comb:
        for dx, dy in flower_offsets:
            nx, ny = x + dx, y + dy
            if (nx, ny) in visited:
                valid = False
                break
            visited.add((nx, ny))
            total_cost += garden[nx][ny]
        if not valid:
            break

    if valid:
        min_cost = min(min_cost, total_cost)

print(min_cost)
