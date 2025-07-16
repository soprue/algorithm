import sys

input = sys.stdin.readline

n = int(input())
postfix = input().strip()
values = [int(input()) for _ in range(n)]

stack = []

for char in postfix:
    if char.isalpha():
        stack.append(values[ord(char) - ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()
        
        if char == "+":
            stack.append(a + b)
        elif char == "-":
            stack.append(a - b)
        elif char == "*":
            stack.append(a * b)
        elif char == "/":
            stack.append(a / b)

print(f"{stack[0]:.2f}")
