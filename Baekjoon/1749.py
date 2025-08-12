import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# N과 M 어느 쪽을 압축 길이로 삼을지 결정 (더 짧은 쪽을 행으로 취급하면 유리)
transpose = False
if N > M:
    # 전치해서 N<=M 형태로 맞추기
    A = list(map(list, zip(*A)))
    N, M = M, N
    transpose = True

answer = -10**18  # 모든 원소가 음수일 수 있으므로 매우 작은 값으로 시작

# top..bottom 행 구간 고정
for top in range(N):
    colSum = [0] * M
    for bottom in range(top, N):
        # 열별 누적합 업데이트
        row = A[bottom]
        for j in range(M):
            colSum[j] += row[j]

        # 1D 최대 부분합 (Kadane) all-negative 대비 위해 -inf 시작
        best = -10**18
        cur = 0
        for v in colSum:
            cur = max(v, cur + v)
            best = max(best, cur)

        answer = max(answer, best)

print(answer)
