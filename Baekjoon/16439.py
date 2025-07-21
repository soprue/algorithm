import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().strip().split())
# 각 회원의 치킨 선호도 정보를 2차원 리스트로 저장
prefers = [list(map(int, input().strip().split())) for _ in range(N)]

max_total = 0

# 치킨 종류 M개 중에서 3개를 고르는 모든 조합을 탐색
for combo in combinations(range(M), 3):
    total = 0
    
    for member in range(N):
        # 현재 회원이 combo에 포함된 3개의 치킨 중에서 가장 선호하는 것 선택
        pick = max(prefers[member][i] for i in combo)
        total += pick
    
    max_total = max(max_total, total)
    
print(max_total)
