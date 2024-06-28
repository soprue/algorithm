from itertools import accumulate
import sys
input = sys.stdin.readline

N, K = map(int, input().split(" "))
S = list(map(int, input().split(" ")))

prefix_sum = [0] + list(accumulate(S))

for _ in range(K):
    A, B = map(int, input().split(" "))
    total_sum = prefix_sum[B] - prefix_sum[A-1]
    avg = total_sum / (B - A + 1)
    print("{:.2f}".format(avg))
