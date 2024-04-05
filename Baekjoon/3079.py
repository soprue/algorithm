# https://www.acmicpc.net/problem/3079

# 이분 탐색으로 푸는 이유: 전체 심사 시간을 기준으로 최소화할 수 있는 값을 찾아야 하기 때문
import sys

# 모든 심사대에 대해 mid 시간 동안 심사받을 수 있는 사람의 수를 계산하는 함수
def is_possible(time, times, M):
    total = sum(time // t for t in times)
    # 계산된 총 처리 인원이 M명 이상인지 여부 반환
    return total >= M

# 최소 심사 시간을 찾는 함수
def min_time(times, M):
    low = 0
    high = max(times) * M # 최대 시간은 가장 긴 심사 시간에 모든 사람이 그 심사대를 이용하는 경우

    while low <= high:
        mid = (low + high) // 2

        if is_possible(mid, times, M):
            high = mid - 1
        else:
            low = mid + 1

    return low

N, M = list(map(int, sys.stdin.readline().strip().split()))
T = list(map(int, [sys.stdin.readline().strip() for _ in range(N)]))

# 계산된 최소 심사 시간 출력
print(min_time(T, M))
