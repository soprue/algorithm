import sys
import re

input = sys.stdin.readline
T = int(input().strip())

pattern = re.compile(r'^[ABCDEF]?A+F+C+[ABCDEF]?$')

for _ in range(T):
    word = input().strip()
    
    if pattern.fullmatch(word):
        print("Infected!")
    else:
        print("Good")
