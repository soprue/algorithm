# https://www.acmicpc.net/problem/1863

import sys

input = sys.stdin.readline

n = int(input())
skylines = [int(input().split()[1]) for _ in range(n)]  # 높이 정보만 저장

stack = []
building_count = 0  # 최소 건물 개수

# 스카이라인이 낮아지는 지점=어떤 빌딩이 그 지점에서 끝났다는 의미 -> 그때 건물 카운트
for y in skylines:
    # 현재 고도가 스택의 최상위 고도보다 작을 때까지 스택에서 팝
    while stack and stack[-1] > y:
        stack.pop()
        building_count += 1  # 새로운 건물 시작

    # 스택이 비어 있거나, 현재 지점의 고도가 스택의 최상위 고도보다 클 때, 현재 고도를 스택에 푸시
    if not stack or stack[-1] < y:
        if y != 0: stack.append(y)

# 스택에 남아 있는 요소는 마지막 건물을 의미
building_count += len(stack)

print(building_count)
