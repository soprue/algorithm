import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().strip().split())
numbers = list(map(int, input().strip().split()))

freq = defaultdict(int) # 값 -> 빈도
left = 0
answer = 0

for right in range(N):
    freq[numbers[right]] += 1
    
    # K 초과 시 왼쪽 포인터 이동하여 초과한 값 줄이기
    # 조건 위반 시 left를 한 번만 옮기고 멈추지 말고, 빈도가 K 이하가 될 때까지 반복해서 옮겨야 함
    while freq[numbers[right]] > K:
        freq[numbers[left]] -= 1
        left += 1
    
    answer = max(answer, right - left + 1)
    
print(answer)
