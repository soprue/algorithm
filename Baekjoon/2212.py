# https://www.acmicpc.net/problem/2212

import sys
input = sys.stdin.readline

# N: 센서의 개수, K: 집중국의 개수
N = int(input())
K = int(input())
sensors = sorted(list(map(int, input().split())))

# 집중국의 수 K가 센서의 수 N과 같거나 클 경우
# 각 센서마다 집중국을 할당할 수 있으므로 수신 가능 영역의 길이의 합은 0
if K >= N:
    print(0)
    sys.exit()

# 센서들 간의 거리를 계산
distances = []
for i in range(1, N):
    distances.append(sensors[i] - sensors[i - 1])
distances.sort(reverse=True)

# 센서들 간 거리가 먼 순서대로 K-1개의 간격을 제거
print(sum(distances[K-1:]))
 
