import sys

input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
s = set(data[1:n+1])
check = data[n+1:]

count = sum(1 for word in check if word in s)
print(count)
