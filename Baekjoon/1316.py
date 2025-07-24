import sys

input = sys.stdin.readline

N = int(input().strip())
result = 0

for _ in range(N):
    word = input().strip()

    seen = set()
    flag = True
    prev = None
    
    for char in word:
        if char != prev:
            if char in seen:
                flag = False
                break
            seen.add(char)
        prev = char
    
    if flag:
        result += 1
        
print(result)
