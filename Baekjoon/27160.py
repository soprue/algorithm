# https://www.acmicpc.net/problem/27160

import sys

N = int(sys.stdin.readline())

CARDS = {}

for _ in range(N):
    S, X = sys.stdin.readline().strip().split()
    CARDS[S] = CARDS.get(S, 0) + int(X)

if 5 in CARDS.values(): print("YES")
else: print("NO")
