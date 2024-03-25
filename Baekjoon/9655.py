# https://www.acmicpc.net/problem/9655

import sys

N = int(sys.stdin.readline().strip())

print("CY" if N % 2 == 0 else "SK")
