import sys

input = sys.stdin.readline

wheels = [list(map(int, input().strip())) for _ in range(4)]
K = int(input())

def rotate(arr, direction):
    if direction == 1:
        return [arr[-1]] + arr[:-1]
    elif direction == -1:
        return arr[1:] + [arr[0]]
    return arr

for _ in range(K):
    num, d = map(int, input().split())
    idx = num - 1

    # 이번 명령에서 각 톱니의 회전 방향
    dirs = [0, 0, 0, 0]
    dirs[idx] = d

    # 왼쪽 톱니바퀴 회전 (idx에서 0까지)
    for i in range(idx, 0, -1):
        if wheels[i][6] != wheels[i - 1][2]:
            dirs[i - 1] = -dirs[i]
        else:
            break

    # 오른쪽 톱니바퀴 회전 (idx에서 끝까지)
    for i in range(idx, 3):
        if wheels[i][2] != wheels[i + 1][6]:
            dirs[i + 1] = -dirs[i]
        else:
            break

    for i in range(4):
        wheels[i] = rotate(wheels[i], dirs[i])

score = 0
if wheels[0][0] == 1: score += 1
if wheels[1][0] == 1: score += 2
if wheels[2][0] == 1: score += 4
if wheels[3][0] == 1: score += 8
print(score)
