# https://www.acmicpc.net/problem/9935

import sys

string = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
stack = []

for char in string:
    stack.append(char)
    # 스택에 문자를 추가할 때마다 스택의 마지막 부분이 bomb와 일치하는지 확인
    if ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

result = ''.join(stack)
print(result if result else "FRULA")
