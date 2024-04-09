# https://www.acmicpc.net/problem/13975

import heapq
import sys
input = sys.stdin.readline

def merge_files(files):
    heapq.heapify(files)
    cost = 0
    
    while len(files) > 1:
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        merged = a + b
        cost += merged
        heapq.heappush(files, merged)
    
    return cost

t = int(input())
for _ in range(t):
    k = int(input())
    files = list(map(int, input().strip().split()))
    print(merge_files(files))
