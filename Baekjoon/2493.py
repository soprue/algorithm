# https://www.acmicpc.net/problem/2493

import sys

N = int(sys.stdin.readline().strip())
towers = list(enumerate(map(int, sys.stdin.readline().strip().split())))

stack = []
answer= [0] * N

for index, height in towers:
    # 스택이 비어 있지 않고, 현재 탑의 높이보다 스택의 top에 있는 탑의 높이가 낮으면
    while stack and stack[-1][1] < height:
        stack.pop()
    
    # 스택이 비어 있지 않다면, 스택의 top에 있는 탑이 현재 탑의 신호를 수신
    if stack:
        answer[index] = stack[-1][0] + 1  # 현재 탑의 신호를 수신하는 탑의 번호 저장
    
    # 현재 탑을 스택에 추가
    stack.append((index, height))

print(' '.join(map(str, answer)))
