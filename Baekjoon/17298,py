# https://www.acmicpc.net/problem/17298

import sys

N = int(sys.stdin.readline().strip())
sequence = list(map(int, sys.stdin.readline().strip().split()))

answer = [-1] * N
stack = []

for i in range(N):
    # 스택이 비어 있지 않고, 현재 요소가 스택의 top에 있는 요소보다 클 경우, 스택의 top에 있는 요소의 오큰수는 현재 요소
    while stack and sequence[stack[-1]] < sequence[i]:
        # 스택에서 요소를 제거하고 결과 리스트에 해당 정보를 업데이트
        answer[stack.pop()] = sequence[i]
    stack.append(i)

print(*answer)
