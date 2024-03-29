# https://www.acmicpc.net/problem/15649

from itertools import permutations

N, M = map(int, input().split())

nums = list(range(1, N + 1))
sequence = list(permutations(nums, M))

for i in sequence:
  for j in i:
    print(j, end=" ")
  print()
