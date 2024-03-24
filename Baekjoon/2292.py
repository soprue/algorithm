# https://www.acmicpc.net/problem/2292

import sys

N = int(sys.stdin.readline().strip())

answer = 1
honeycomb = 1

while N > honeycomb :
    honeycomb += 6 * answer
    answer += 1

print(answer)
