import sys

N = int(sys.stdin.readline().strip())
_N = sorted(list(map(int, sys.stdin.readline().strip().split())))
M = int(sys.stdin.readline().strip())
_M = list(map(int, sys.stdin.readline().strip().split()))

DICT = {}

for n in _N:
    if n in DICT:
        DICT[n] += 1
    else:
        DICT[n] = 1

for m in _M:
  if m in DICT:
    print(DICT[m], end=' ')
  else:
     print(0, end=' ')