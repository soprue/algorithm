# https://www.acmicpc.net/problem/2295

# x + y + z = k는 x + y = k - z와 같다.
# 1. x + y 합을 집합에 모두 넣어 둠
# 2. 탐욕적 접근으로 k가 가장 큰 수부터 오게끔 역으로 접근
# 3. k - z가 sum_XY에 존재한다면 print

import sys

N = int(sys.stdin.readline().strip())
U = [int(sys.stdin.readline().strip()) for _ in range(N)]
U.sort() 

sum_XY = set()
for x in range(N):
    for y in range(x, N): # x부터 시작하여 중복 허용 조합 고려
        sum_XY.add(U[x] + U[y])

for z in range(N-1, -1, -1):
    for k in range(z + 1):
        if U[z] - U[k] in sum_XY:
            print(U[z])
            sys.exit(0)
