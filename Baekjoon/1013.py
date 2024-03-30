# https://www.acmicpc.net/problem/1013

import re
t = int(input())

for _ in range(t):
    s = input().strip()
    regex = re.compile('(100+1+|01)+')
    
    if regex.fullmatch(s):
        print('YES')
    else:
        print('NO')
