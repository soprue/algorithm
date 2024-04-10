# https://www.acmicpc.net/problem/1107

import sys

n = int(input())
m = int(input())
broken = set(input().split()) if m else set()

if n == 100:
    print(0)
    sys.exit(0)

# 1. 현재 채널(100번)에서 +, - 버튼만 사용하는 경우
min_press = abs(100 - n)

# 2. 숫자 버튼을 사용하여 채널 N에 접근하는 경우
for channel in range(1000001):
    for c in str(channel):
        if c in broken:  # 현재 채널에 고장난 버튼이 포함되어 있으면 다음 채널로
            break
    else:
        # 숫자 버튼을 누른 횟수 + (+, -) 버튼을 누른 횟수
        press = len(str(channel)) + abs(channel - n)
        min_press = min(min_press, press)

print(min_press)
