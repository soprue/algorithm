# https://www.acmicpc.net/problem/15686

import sys
from itertools import combinations

def calculate_chicken_distance(houses, chicken_stores):
    total_distance = 0
    for house in houses:
        distance = min([abs(house[0]-chicken[0]) + abs(house[1]-chicken[1]) for chicken in chicken_stores])
        total_distance += distance
    return total_distance

N, M = map(int, sys.stdin.readline().strip().split())

city = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
houses = []
chicken = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chicken.append((r, c))

chicken_combinations = list(combinations(chicken, M))

min_distance = float('inf')
for comb in chicken_combinations:
    distance = calculate_chicken_distance(houses, comb)
    min_distance = min(min_distance, distance)

print(min_distance)
