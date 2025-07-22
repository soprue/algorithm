import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input().strip())
hints = []

for _ in range(N):
    nums, strike, ball = map(int, input().strip().split())
    hints.append((str(nums), strike, ball))
    
candidates = list(permutations(range(1, 10), 3))

for q_num, q_s, q_b in hints:
    new_candidates = []
    
    for c in candidates:
        strike = ball = 0
        for i in range(3):
            if int(q_num[i]) == c[i]:
                strike += 1
            elif int(q_num[i]) in c:
                ball += 1
            
        if strike == q_s and ball == q_b:
            new_candidates.append(c)
    
    candidates = new_candidates
    
print(len(candidates))
