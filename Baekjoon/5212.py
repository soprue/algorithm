import sys

input = sys.stdin.readline

R, C = map(int, input().strip().split())
grid = [list(input().strip()) for _ in range(R)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

sink = []
for r in range(R):
    for c in range(C):
        if grid[r][c] == 'X':
            count = 0

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (nr < 0 or nc < 0 or nr >= R or nc >= C) or grid[nr][nc] == '.':
                    count += 1

            if count >= 3:
                sink.append((r, c))
                
new = [['.'] * C for _ in range(R)]
for r in range(R):
    for c in range(C):
        if grid[r][c] == 'X' and (r, c) not in sink:
            new[r][c] = 'X'

top_r = R
bottom_r = -1
left_c = C
right_c = -1

for i in range(R):
    for j in range(C):
        if new[i][j] == 'X':
            if i < top_r: top_r = i
            if i > bottom_r: bottom_r = i
            if j < left_c: left_c = j
            if j > right_c: right_c = j

for i in range(top_r, bottom_r + 1):
    print(''.join(new[i][left_c:right_c + 1]))
