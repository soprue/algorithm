# https://www.acmicpc.net/problem/1193

# 라인에 있는 분수의 개수는 1라인은 1개, 2라인은 2개, 3라인은 3개, 4라인은 4개...
# 짝수 라인: 분모가 1씩 늘어나고 분자가 1씩 줄어듦
# 홀수 라인: 분자가 1씩 늘어나고 분모가 1씩 줄어듦

import sys

X = int(sys.stdin.readline().strip())

line = 0
end = 0 # 그 라인의 마지막 인덱스 ( 1, 3, 6, 10 ... )

while X > end:
    line += 1
    end += line

diff = end - X

if line % 2 == 0 :
    top = line - diff
    bottom = diff + 1
else :
    top = diff + 1
    bottom = line - diff

print(f'{top}/{bottom}')
