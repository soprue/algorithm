# https://www.acmicpc.net/problem/17299

import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 각 원소의 빈도 수 계산
count = Counter(A)
# 결과를 저장할 리스트, 초기값은 -1
result = [-1] * N
# 이전 원소들의 인덱스를 관리할 스택
stack = []

# 수열의 각 원소에 대해 오등큰수 찾기
for i in range(N):
    # 스택이 비어 있지 않고, 현재 원소의 빈도 수가 스택의 top 원소의 빈도 수보다 클 때
    while stack and count[A[i]] > count[A[stack[-1]]]:
        # 스택에서 pop한 원소의 오등큰수는 현재 원소
        result[stack.pop()] = A[i]
    # 현재 원소의 인덱스를 스택에 push
    stack.append(i)

print(*result)
