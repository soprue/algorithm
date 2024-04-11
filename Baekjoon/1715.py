# https://www.acmicpc.net/problem/1715

import heapq
import sys
input = sys.stdin.readline

N = int(input())
cards = [int(input()) for _ in range(N)]
heapq.heapify(cards)

result = 0
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    sum = a + b
    
    result += sum
    heapq.heappush(cards, sum)
    
print(result)
