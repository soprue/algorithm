# https://www.acmicpc.net/problem/7785
# 추가/삭제 연산이 많을 때는 연산이 빠 딕셔너리(해시맵) 구조를 이용해야 함

import sys

N = int(sys.stdin.readline().strip())

company = {}

for _ in range(N) :
    name, status = sys.stdin.readline().strip().split()
    if status == "enter" :
        company[name] = True
    else:
        del company[name]

print("\n".join(sorted(company.keys(), reverse=True)))
