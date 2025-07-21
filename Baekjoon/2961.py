import sys

input = sys.stdin.readline

N = int(input())
items = [tuple(map(int, input().strip().split())) for _ in range(N)]

# 최소 차이를 저장할 변수
# 처음에는 무한대로 설정해두고, 이후 더 작은 값이 나오면 갱신
min_diff = float('inf')

# 1부터 2^N - 1까지 반복해서, 모든 부분집합을 비트마스크로 탐색 (공집합은 제외)
for bit in range(1, 1 << N):
    sour = 1
    bitter = 0
    
    # N개의 재료 중 어떤 재료를 선택했는지 확인
    for i in range(N):
        # 비트마스크를 활용해서, 현재 조합(bit)에서 i번째 재료가 선택됐는지 확인
        if bit & (1 << i):
            s, b = items[i]
            sour *= s
            bitter += b
            
    diff = abs(sour - bitter)
    min_diff = min(min_diff, diff)
    
print(min_diff)
