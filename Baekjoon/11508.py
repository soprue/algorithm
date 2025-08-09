import sys
input = sys.stdin.readline

N = int(input().strip())
prices = [int(input().strip()) for _ in range(N)]
prices.sort(reverse=True)

# 전체합 - (3번째마다 오는 공짜들의 합)
answer = sum(prices) - sum(prices[2::3])
print(answer)
