# https://www.acmicpc.net/problem/2559

# 연속적인 K일 간의 온도 합을 최대로 하는 것을 찾아야 함
# 슬라이딩 윈도우를 사용하여 처음 K일의 합을 구하고,
# 그 다음날부터는 매번 윈도우의 맨 앞 데이터를 빼고 새로운 데이터를 더하는 방식으로 계속 윈도우를 이동시키면서 최대값을 갱신해 나감

import sys
input = sys.stdin.readline

# N: 온도를 측정한 전체 날짜의 수, K: 합을 구하기 위한 연속적인 날짜의 수
N, K = map(int, input().split())  
temperatures = list(map(int, input().split()))

# 첫 K일의 온도 합 초기화
current_sum = sum(temperatures[:K])
max_sum = current_sum  # 최대 온도 합 초기화

# 슬라이딩 윈도우 기법 적용
for i in range(K, N):
    current_sum += temperatures[i]  # 현재 윈도우의 끝에 새로운 온도 추가
    current_sum -= temperatures[i - K]  # 현재 윈도우의 시작에 있던 온도 제거
    max_sum = max(max_sum, current_sum)  # 최대 온도 합 갱신

print(max_sum)
