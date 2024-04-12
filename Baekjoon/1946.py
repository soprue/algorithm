# https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    applicants = []

    # 지원자 정보 입력 받기
    for _ in range(N):
        paper, interview = map(int, input().strip().split())
        applicants.append((paper, interview))

    hire = 0
    best_interview = N + 1 # 최고 면접 순위 초기화
    
    # 서류 순위 기준으로 오름차순 정렬
    applicants.sort()
    for paper, interview in applicants:
        # 현재 지원자의 면접 순위가 이전 지원자들의 면접 순위 중 최고 순위보다 좋다면 선발
        if interview < best_interview:
            hire += 1
            best_interview = interview

    print(hire)
    
