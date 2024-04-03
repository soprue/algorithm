# https://www.acmicpc.net/problem/2346

import sys
from collections import deque

N = int(sys.stdin.readline().strip())
# enumerate를 사용하여 각 풍선에 번호 붙임
balloons = deque(enumerate(map(int, sys.stdin.readline().strip().split())))
answer = []

for _ in range(N):
    index, next = balloons.popleft()
    answer.append(index + 1)

    if next > 0:
        # rotate(음수) -> 왼쪽 회전
        # next가 양수일 때는 이미 현재 풍선을 제외하고 이동해야 하므로, next - 1만큼 회전
        balloons.rotate(-(next - 1))
    elif next < 0:
        # rotate(양수) -> 오른쪽 회전
        # next가 음수의 경우는 현재 풍선을 포함하지 않으므로 그대로 next만큼 회전
        balloons.rotate(-(next))

print(' '.join(map(str, answer)))
