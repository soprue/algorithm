import sys
input = sys.stdin.readline

N, K = map(int, input().split())
medal = []

for _ in range(N):
    number, gold, silver, bronze = map(int, input().split())
    medal.append((number, gold, silver, bronze))

sorted_medal = sorted(medal, key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1
prev_medals = None
country_rank = {}

for i, data in enumerate(sorted_medal):
    country_id, gold, silver, bronze = data
    current_medals = (gold, silver, bronze)

    if current_medals != prev_medals:
        rank = i + 1
        prev_medals = current_medals
    
    country_rank[country_id] = rank

print(country_rank[K])
