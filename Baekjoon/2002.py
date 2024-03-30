# https://www.acmicpc.net/problem/2002

import sys

N = int(sys.stdin.readline().strip())

enter = dict()
for i in range(N):
    car = sys.stdin.readline().strip()
    enter[car] = i

out = [sys.stdin.readline().strip() for _ in range(N)]

overtaking = 0

for i in range(N - 1):
	for j in range(i + 1, N):
		# 나오는 차량의 들어올 때 인덱스가 이후 차량들의 들어올 때 인덱스보다 하나라도 클 경우 추월한 것으로 간주
		if enter[out[i]] > enter[out[j]]:
			overtaking += 1
			break
		
print(overtaking)
