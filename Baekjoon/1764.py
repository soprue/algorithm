# https://www.acmicpc.net/problem/1764

import sys

N, M = map(int, sys.stdin.readline().strip().split())
_N = set([sys.stdin.readline().strip() for _ in range(N)])
_M = set([sys.stdin.readline().strip() for _ in range(M)])

intersection = sorted(_N & _M)
print(len(intersection))
print("\n".join(sorted(intersection)))
