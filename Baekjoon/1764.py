# https://www.acmicpc.net/problem/1764

import sys

input_lines = sys.stdin.readlines()
N, M = map(int, input_lines[0].strip().split())

_N = set([line.strip() for line in input_lines[1:N + 1]])
_M = set([line.strip() for line in input_lines[N + 1:]])

intersection = sorted(_N & _M)
print(len(intersection))
print("\n".join(sorted(intersection)))
