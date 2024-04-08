# https://www.acmicpc.net/problem/14235

import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    a = list(map(int, input().strip().split()))

    if a[0] == 0:
        print(abs(heapq.heappop(heap)) if heap else -1)
    else:
        for i in range(1, a[0] + 1):
            heapq.heappush(heap, -a[i])
