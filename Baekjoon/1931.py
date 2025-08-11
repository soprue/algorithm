import sys

input = sys.stdin.readline

N = int(input().strip())
meetings = [tuple(map(int, input().strip().split())) for _ in range(N)]

# 회의들을 끝나는 시간 오름차순, 같다면 시작 시간 오름차순으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end = 0

for start, end in meetings:
    if start >= last_end:
        count += 1
        last_end = end
        
print(count)
