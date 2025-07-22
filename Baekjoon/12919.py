import sys

input = sys.stdin.readline

S = input().strip()
T = input().strip()

result = 0

def dfs(current):
    global result
    
    if current == S:
        result = 1
        return
    
    if len(current) < len(S):
        return
    
    # 마지막 문자가 'A'면 A 제거
    if current[-1] == "A":
        dfs(current[:-1])
    
    # 첫 문자가 'B'면 뒤집고 B 제거
    if current[0] == "B":
        dfs(current[1:][::-1])
    
dfs(T)
print(result)
