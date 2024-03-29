# https://www.acmicpc.net/problem/15650

from itertools import combinations

N, M = map(int, input().split())

nums = list(range(1, N + 1))
orders = combinations(nums, M)
    
for i in orders:
  for j in i:
    print(j, end=" ")
  print()
