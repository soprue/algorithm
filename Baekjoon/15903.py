# https://www.acmicpc.net/problem/15903
from heapq import *

N, M = list(map(int, input().strip().split()))
cards = list(map(int, input().strip().split()))
heapify(cards)  # 카드 리스트를 최소 힙으로 변환

for _ in range(M):
    x = heappop(cards)  # x: 가장 작은 카드
    y = heappop(cards)  # y: 두 번째로 작은 카드
    z = x + y

    # 계산한 값을 x번 카드와 y번 카드 두 장 모두에 덮어 씀
    heappush(cards, z) 
    heappush(cards, z)

print(sum(cards))
