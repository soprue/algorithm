import sys

input = sys.stdin.readline

H, W = map(int, input().split())
N = int(input())

stickers = [tuple(map(int, input().split())) for _ in range(N)]

max_area = 0

for i in range(N):
    for j in range(i + 1, N):
        r1, c1 = stickers[i]
        r2, c2 = stickers[j]
        
        # 각 스티커를 회전 안 한 경우와 회전한 경우 모두 고려 (2x2=4가지)
        for a1, b1 in [(r1, c1), (c1, r1)]:
            for a2, b2 in [(r2, c2), (c2, r2)]:
                
                # 가로로 나란히 놓기
                if max(a1, a2) <= H and (b1 + b2) <= W:
                    area = a1 * b1 + a2 * b2
                    max_area = max(max_area, area)
                    
                # 세로로 나란히 놓기 
                if max(b1, b2) <= W and (a1 + a2) <= H:
                    area = a1 * b1 + a2 * b2
                    max_area = max(max_area, area)
                    
print(max_area)
