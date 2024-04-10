# https://www.acmicpc.net/problem/2512

n = int(input())
budgets = list(map(int, input().strip().split()))
m = int(input())

low = 0
high = max(budgets)

while low <= high:
    mid = (low + high) // 2 # 중간값을 상한액으로 가정
    sum = 0 # 상한액을 적용했을 때의 총 예산 합계

    for budget in budgets:
        if budget > mid: # 상한액보다 큰 요청에는 상한액을 적용
            sum += mid
        else: # 상한액 이하의 요청에는 원래 요청 금액을 적용
            sum += budget

    if sum > m: # 총 예산을 초과하는 경우 상한액을 낮춤
        high = mid - 1
    else: # 총 예산 이하인 경우 상한액을 높임
        low = mid + 1

print(high)
