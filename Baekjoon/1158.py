# https://www.acmicpc.net/problem/1158

from collections import deque

n, k = map(int, (input().strip().split()))

list = deque([i+1 for i in range(n)])
answer = []

while list:
    list.rotate(-(k - 1))
    answer.append(list.popleft())

print(f'<{", ".join(map(str, answer))}>')
