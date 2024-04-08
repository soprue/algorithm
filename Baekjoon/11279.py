# https://www.acmicpc.net/problem/11279

import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(heap, -x)
    else:
        print(abs(heapq.heappop(heap)) if heap else 0)
