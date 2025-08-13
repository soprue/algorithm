import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
A = [list(map(int, input().strip().split())) for _ in range(N)]

answer = -10**18

def kadane(arr):
  best = -10**18
  current = 0

  for x in arr:
    current = max(x, current + x)
    best = max(best, current)

  return best

# top: 시작 행, bottom: 끝 행
for top in range(N):
  # colSum[j] = top~bottom 사이에서 i번째 열의 합
  colSum = [0] * M
  for bottom in range(top, N):
    # 현재 bottom 행을 합산해서 colSum 갱신
    row = A[bottom]
    for i in range(M):
      colSum[i] += row[i]

    # colSum에서 "연속된 열 구간"의 최댓값 = (top..bottom) x (어떤 열 구간)의 최댓 직사각형 합
    answer = max(answer, kadane(colSum))

print(answer)
