# https://www.acmicpc.net/problem/2675

import sys

N = int(sys.stdin.readline().strip())

for _ in range(N) :
    R, S = sys.stdin.readline().strip().split()
    for x in S :
        print(x * int(R), end="")
    print()
