import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

i = j = 0
result = []

while i < N and j < M:
    if A[i] <= B[j]:
        result.append(A[i])
        i += 1
    else:
        result.append(B[j])
        j += 1
        
# 남은 요소 추가
result.extend(A[i:])
result.extend(B[j:])

print(' '.join(map(str, result)))
