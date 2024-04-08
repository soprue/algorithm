# https://www.acmicpc.net/problem/2884

hour, min = map(int, input().split())
min = min - 45

if min < 0:
    min += 60
    hour = hour - 1 if hour > 0 else 23

print(hour, min)
