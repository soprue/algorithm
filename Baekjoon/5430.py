# https://www.acmicpc.net/problem/5430

import sys
from collections import deque

def AC(arr, p):
    command = list(p)
    reverse = False  # 배열 뒤집기 상태 플래그
    
    for cmd in command:
        if cmd == 'R':  # 뒤집기 연산
            reverse = not reverse  # 뒤집기 상태 토글
        elif cmd == 'D':  # 버리기 연산
            if not arr:  # 배열이 비어 있으면 에러
                return 'error'
            if reverse:  # 뒤집힌 상태면 뒤에서 요소 제거
                arr.pop()
            else:  # 뒤집히지 않은 상태면 앞에서 요소 제거
                arr.popleft()
                
    if reverse:  # 모든 연산 후 뒤집힌 상태면 리스트를 뒤집어서 반환
        arr.reverse()
        
    return "[" + ",".join(map(str, arr)) + "]"
    

T = int(sys.stdin.readline().strip())

for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    arr = sys.stdin.readline().strip()[1:-1]
    if arr:
        arr = deque(map(int, arr.split(',')))
    else:
        arr = deque() 
    print(AC(arr, p))
