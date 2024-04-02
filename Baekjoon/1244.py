# https://www.acmicpc.net/problem/1244
import sys

def operation(switches, gender, number):
    index = number - 1
    
    if gender == 1:
        for i in range(index, len(switches), number):
            switches[i] = 1 - switches[i]
    elif gender == 2:
        switches[index] = 1 - switches[index]
        for i in range(1, len(switches)//2 + 1):
            # 리스트 인덱스를 벗어나는지 확인
            if index - i < 0 or index + i >= len(switches):
                break
            # 좌우대칭 확인
            if switches[index - i] != switches[index + i]:
                break
            switches[index - i] = 1 - switches[index - i]
            switches[index + i] = 1 - switches[index + i]
            
    return switches

N = int(sys.stdin.readline().strip())
switches = list(map(int, sys.stdin.readline().split()))

students = int(sys.stdin.readline().strip())

for _ in range(students):
    gender, number = map(int, sys.stdin.readline().split())
    operation(switches, gender, number)

for i, switch in enumerate(switches, start=1):
    print(switch, end=' ')
    if i % 20 == 0:
        print()
