import sys

input = sys.stdin.readline

N = int(input().strip())

# 1원, 3원은 2원/5원 조합으로 만들 수 없음 → 정답 없음
if N in (1, 3):
    print(-1)
    exit(0)

count = 0

# 5원을 최대한 많이 쓰면 동전 개수를 최소화할 수 있음
# → N이 5로 나누어떨어질 때까지 2원짜리 하나씩 사용
while N % 5 != 0:
    N -= 2
    count += 1
    
count += N // 5

print(count)
