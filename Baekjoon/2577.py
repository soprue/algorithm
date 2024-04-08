# https://www.acmicpc.net/problem/2577

from collections import Counter

a = int(input())
b = int(input())
c = int(input())

result = a * b * c
result = Counter(str(result))

for i in range(0, 10):
    print(result[str(i)])
