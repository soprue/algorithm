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

def binary(m, _N, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if m == _N[mid]:
        return DICT[m]
    elif m < _N[mid]:
        return binary(m, _N, start, mid - 1)
    else:
        return binary(m, _N, mid + 1, end)


for m in _M:
  print(binary(m, _N, 0, len(_N)-1), end=' ')