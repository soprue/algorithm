# https://www.acmicpc.net/problem/2908

A, B = input().split()
A = int(A[::-1])
B = int(B[::-1])

print(max([A, B]))
