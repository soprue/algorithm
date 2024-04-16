# https://www.acmicpc.net/problem/1463

n = int(input())
dp = [0] * (n + 1) # 연산 횟수를 저장할 리스트

# 각 숫자에 대해 가능한 모든 연산을 고려하고, 그 중에서 최소 연산 횟수를 선택하여 저장
for i in range(2, n + 1):
    # 기본적으로 1을 빼는 연산을 수행한 경우를 초기값으로 설정
    dp[i] = dp[i - 1] + 1

    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])
