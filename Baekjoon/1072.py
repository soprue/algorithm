# https://www.acmicpc.net/problem/1072

x, y = map(int, input().split())

def win_rate(X, Y):
    return (Y * 100) // X

left = 0
right = 1000000000
current_rate = win_rate(x, y)
result = -1

while left <= right:
    mid = (left + right) // 2
    new_rate = win_rate(x + mid, y + mid)

    # 새로운 승률이 현재 승률보다 높아지는 경우
    if new_rate > current_rate:
        result = mid
        right = mid - 1 # 더 작은 범위를 탐색하기 위해 right 조정
    else:
        left = mid + 1 # 승률이 변하지 않으면, 더 많은 게임이 필요함을 의미하므로 left 조정

print(result)
