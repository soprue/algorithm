import sys

input = sys.stdin.readline

n = int(input().strip())
# 1번 인덱스부터 쓰기 위해 앞에 0을 하나 붙임
glasses = [0] + [int(input().strip()) for _ in range(n)]

if n == 1:
  print(glasses[1])
elif n == 2:
  print(glasses[1] + glasses[2])
else:
  dp = [0] * (n + 1)

  dp[1] = glasses[1]
  dp[2] = glasses[1] + glasses[2]

  for i in range(3, n + 1):
    dp[i] = max(
      dp[i - 1],                                  # i 안 마심
      dp[i - 2] + glasses[i],                     # i만 마심 (i-1은 안 마심)
      dp[i - 3] + glasses[i - 1] + glasses[i]     # i-1, i 마심 (i-2는 안 마심)
    )

  print(dp[n])
