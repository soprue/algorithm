import sys

input = sys.stdin.readline

str = input().strip()
stack = []

for char in str:
    if char == "(" or char == "[":
        stack.append(char)
    elif char == ")":
        temp = 0
        while stack:
            top = stack.pop()
            if top == "(":
                stack.append(2 if temp == 0 else 2 * temp)
                break
            elif isinstance(top, int):
                temp += top
            else:
                print(0)
                exit(0)
        else:  # ← 스택 다 돌았는데 '(' 못 찾음
            print(0)
            exit(0)
    elif char == "]":
        temp = 0
        while stack:
            top = stack.pop()
            if top == "[":
                stack.append(3 if temp == 0 else 3 * temp)
                break
            elif isinstance(top, int):
                temp += top
            else: 
                print(0)
                exit(0)
        else:  # ← 스택 다 돌았는데 '[' 못 찾음
            print(0)
            exit(0)
    
result = 0
for item in stack:
    if isinstance(item, int):
        result += item
    else: 
        print(0)
        exit(0)
        
print(result)
