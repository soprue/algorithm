# https://www.acmicpc.net/problem/2805

def cutting(heights, M):
    low = 0
    high = max(heights) # 나무 높이의 최댓값

    while low <= high:
        mid = (low + high) // 2
        total = sum((h - mid) for h in heights if h > mid)
        
        
        # 만약 얻은 나무의 길이가 필요한 길이 M 이상이라면,
        # 더 높은 높이에서도 조건을 만족할 수 있는지 확인하기 위해 low를 mid + 1로 조정하여 탐색 범위를 조정
        if total >= M:
            low = mid + 1
        else:
            high = mid - 1

    return high

N, M = map(int, input().split())
heights = list(map(int, input().split()))

print(cutting(heights, M))
