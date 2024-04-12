# https://www.acmicpc.net/problem/1406

# 삭제(del)와 삽입(insert) 연산을 사용하면 시간 초과가 남 -> 스택으로 구현

import sys
input = sys.stdin.readline

string = list(input().strip())
# 왼쪽 스택은 초기 문자열을 그대로 사용
left = string
# 오른쪽 스택은 비어있음
right = []

# 명령어 개수 입력
M = int(input())
for _ in range(M):
    command = input().strip().split()
    
    if command[0] == "L":
        if left:
            right.append(left.pop())
    elif command[0] == "D":
        if right:
            left.append(right.pop())
    elif command[0] == "B":
        if left:
            left.pop()
    elif command[0] == "P":
        left.append(command[1])

# 명령어 처리 후 왼쪽 스택과 뒤집은 오른쪽 스택을 합쳐서 출력
print(''.join(left + right[::-1]))
