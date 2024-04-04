# https://www.acmicpc.net/problem/2075

import sys
import heapq

N = int(sys.stdin.readline().strip())
heap = []

for _ in range(N):
    numbers = map(int, input().split())

    for number in numbers:
        if len(heap) < N: # heap의 크기를 n개로 유지
            heapq.heappush(heap, number)
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)

print(heap[0])
