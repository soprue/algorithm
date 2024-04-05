# https://www.acmicpc.net/problem/2110

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]

# 집의 위치를 오름차순으로 정렬
houses.sort()

low = 1 # 가능한 최소 거리
high = houses[-1] - houses[0] # 탐색할 "공유기 사이의 거리"에 대한 최대 가능 범위를 설정

while low <= high:
    mid = (low + high) // 2  
    current = houses[0]
    count = 1  # 첫 번째 집에 공유기 설치

    # 선택한 mid 값을 "공유기 사이의 최소 거리"로 가정하고, 이 거리를 유지하며 공유기를 설치할 수 있는지를 확인
    for i in range(1, N):
        if houses[i] >= current + mid:
            count += 1
            current = houses[i]

    # 설치할 수 있는 공유기 수에 따라 거리 조정
    if count >= C:  # 공유기를 더 많이 또는 충분히 설치할 수 있는 경우
        low = mid + 1
    else:  # 공유기를 충분히 설치할 수 없는 경우
        high = mid - 1

# 가장 인접한 두 공유기 사이의 최대 거리 출력
print(high)
