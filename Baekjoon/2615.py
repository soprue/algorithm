# https://www.acmicpc.net/problem/2615
import sys

length = 19
board = [list(map(int, sys.stdin.readline().split())) for _ in range(length)]
direction = [(0, 1), (1, 1), (1, 0), (1, -1)]

def isWin(i, j, color, dx, dy):
    count = 1
    stones = [(i, j)]
    
    # 연속된 알 체크
    x, y = i + dx, j + dy
    while 0 <= x < length and 0 <= y < length and board[x][y] == color:
        count += 1
        stones.append((x, y))
        x += dx
        y += dy
        
    # 5목 확인 및 6목 체크
    if count == 5:
        # 연속된 돌의 양 끝점 검사
        prev_x, prev_y = i - dx, j - dy  # 연속된 돌의 시작점의 이전 위치
        next_x, next_y = x, y  # 연속된 돌의 마지막 돌의 다음 위치

        # 시작점의 이전이나 마지막의 다음에 같은 색 돌이 없으면 5목으로 인정
        if not (0 <= prev_x < length and 0 <= prev_y < length and board[prev_x][prev_y] == color) and \
           not (0 <= next_x < length and 0 <= next_y < length and board[next_x][next_y] == color):
            return True, stones
    return False, []

winner = None
win_stones = []

for i in range(length):
    for j in range(length):
        if board[i][j] == 0: continue
        for dx, dy in direction:
            win, stones = isWin(i, j, board[i][j], dx, dy)
            if win:
                stones_sorted = sorted(stones, key=lambda stone: (stone[1], stone[0]))
                if not winner:
                    winner = board[i][j]
                    win_stones = stones_sorted
                else:
                    if stones_sorted[0] < win_stones[0]:
                        win_stones = stones_sorted

if winner and win_stones:
    print(winner)
    print(win_stones[0][0] + 1, win_stones[0][1] + 1)
else:
    print(0)
