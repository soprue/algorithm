# https://www.acmicpc.net/problem/9095

T = int(input())
max_n = 10 # 문제 조건: n < 11

dp = [0] * (max_n + 1)
if max_n >= 1:
    dp[1] = 1
if max_n >= 2:
    dp[2] = 2
if max_n >= 3:
    dp[3] = 4

for i in range(4, max_n + 1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
    n = int(input())
    print(dp[n])
