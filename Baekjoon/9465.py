# https://www.acmicpc.net/problem/9465

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # n: 스티커 열의 수
    n = int(input())
    dp = [list(map(int, input().strip().split())) for _ in range(2)]

    # 지그재그의 경로로 스티커를 떼는 경우가 점수의 최댓값을 얻는 경우
    # 지그재그로 가는 경우와 지그재그 후 한 칸 건너뛰는 경우를 비교하며 DP값을 저장한 후 최댓값 구함
    if n > 1 :
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    for i in range(2, n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][n-1], dp[1][n-1]))
