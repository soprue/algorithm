# https://www.acmicpc.net/problem/3052

result = set()

for _ in range(10):
    x = int(input())
    result.add(x % 42)

print(len(result))
