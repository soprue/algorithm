import sys

input = sys.stdin.readline

N, X = map(int, input().split())
hits = list(map(int, input().split()))

current = sum(hits[:X])
max_hits = current
max_period = 1

for i in range(X, N):
    # current = 이전 구간 합 + 새 값 - 빠진 값
    current += hits[i] - hits[i - X]
    
    if current > max_hits:
        max_hits = current
        max_period = 1
    elif current == max_hits:
        max_period += 1
        
if max_hits == 0:
    print("SAD")
else:
    print(max_hits)
    print(max_period)
