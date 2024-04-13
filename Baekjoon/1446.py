# https://www.acmicpc.net/problem/1446

import sys
input = sys.stdin.readline

# N: 지름길 개수, D: 고속도로 길이
N, D = map(int, input().split())
shortcuts = [list(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(D+1)]
for i in range(1, D+1):
    dp[i] = dp[i-1] + 1
    
    for j in range(N):
        # 현재 위치에서 시작하는 지름길이 있는 경우
        if shortcuts[j][1] == i:
            dp[i] = min(dp[i], dp[shortcuts[j][0]] + shortcuts[j][2])
            
print(dp[D])
