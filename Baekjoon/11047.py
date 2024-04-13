# https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline

# N: 동전 종류 수, K: 목표 금액
N, K = map(int, input().strip().split())
coins = [int(input().strip()) for _ in range(N)]

count = 0  # 사용된 동전의 총 개수

# 가장 큰 가치의 동전부터 시작
for coin in reversed(coins):
    if K == 0:
        break
    if coin > K:
        continue
    count += K // coin  # 현재 동전으로 만들 수 있는 최대 개수
    K %= coin  # 남은 금액 업데이트

print(count)
