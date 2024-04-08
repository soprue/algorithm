# https://www.acmicpc.net/problem/19638

import sys
import heapq

input = sys.stdin.readline

# n: 거인의 수, h: 센티의 키, t: 뿅망치 사용 횟수 제한
n, h, t = map(int, input().split())

# 거인들의 키를 음수로 변환하여 리스트에 저장
giants = [-int(input()) for _ in range(n)]
heapq.heapify(giants)

# 뿅망치 사용 횟수
count = 0

for i in range(t):
    # 힙의 최댓값이 1이거나 센티의 키보다 작으면 반복 중단
    if -giants[0] == 1 or -giants[0] < h:
        break
    else:
        # heapreplace: 힙의 최댓값을 새로운 값으로 교체한 후 힙을 다시 정렬
        heapq.heapreplace(giants, -(-giants[0] // 2))
        count += 1

if -giants[0] >= h:
    print('NO')
    print(-giants[0])
else:
    print('YES')
    print(count)
