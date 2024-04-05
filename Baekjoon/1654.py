# https://www.acmicpc.net/problem/1654

n, k = map(int, input().split())
lines = [int(input()) for _ in range(n)]

answer = 1 # 정답은 항상 1 이상
left = 1
right = 2 ** 31 - 1 # 전선 최대 길이

while left <= right:
    mid = (left + right) // 2
    count = 0

    for line in lines:
        count += line // mid # 전선 길이로 나눈 몫이 만들 수 있는 전선의 개수
    if count >= k: # k개 이상 전선을 만들 수 있으면 정답을 갱신
        answer = mid
        left = mid + 1
    else: # k개 이상 전선을 만들 수 없으면 랜선을 더 잘게 쪼개야 함
        right = mid - 1

print(answer)
