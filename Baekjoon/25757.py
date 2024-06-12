from math import floor
import sys

input = sys.stdin.readline

n, game = input().split()
n = int(n)

# 게임 타입에 따른 참가자 수를 사전으로 매핑
game_to_participants = {'Y': 2, 'F': 3, 'O': 4}
participants = game_to_participants[game]

people = {input().strip() for _ in range(n)}

print(floor(len(people) / (participants - 1)))
