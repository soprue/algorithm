import sys

input = sys.stdin.readline
L, R = input().strip().split()
word = input().strip()

pos = {
    'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4),
    'y': (0, 5), 'u': (0, 6), 'i': (0, 7), 'o': (0, 8), 'p': (0, 9),
    'a': (1, 0), 's': (1, 1), 'd': (1, 2), 'f': (1, 3), 'g': (1, 4),
    'h': (1, 5), 'j': (1, 6), 'k': (1, 7), 'l': (1, 8),
    'z': (2, 0), 'x': (2, 1), 'c': (2, 2), 'v': (2, 3),
    'b': (2, 4), 'n': (2, 5), 'm': (2, 6),
}

left_set = set("qwertasdfgzxcv")

left_pos = pos[L]
right_pos = pos[R]

total = 0

for char in word:
    tx, ty = pos[char] 

    if char in left_set:
        cx, cy = left_pos
        total += abs(cx - tx) + abs(cy - ty) + 1  
        left_pos = (tx, ty)                      
    else:
        cx, cy = right_pos
        total += abs(cx - tx) + abs(cy - ty) + 1
        right_pos = (tx, ty)                      

print(total)
