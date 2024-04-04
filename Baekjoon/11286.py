# https://www.acmicpc.net/problem/11286

import sys
from heapq import *

N = int(sys.stdin.readline().strip())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline().strip())
    
    if x == 0:
        print(heappop(heap)[1] if heap else 0)
    else:
        # 힙에 (절댓값, 원본값)의 튜플로 값을 추가
        # 이렇게 함으로써 절댓값이 같은 원소가 여러 개 있을 경우 원본값이 작은 것부터 정렬됨
        heappush(heap, (abs(x), x))
