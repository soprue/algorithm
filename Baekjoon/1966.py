# https://www.acmicpc.net/problem/1966

import sys
from collections import deque

def find_print_order(docs, index):
    # 문서들을 (중요도, 인덱스) 형태로 deque에 저장
    queue = deque([(doc, idx) for idx, doc in enumerate(docs)])
    order = 0  # 인쇄 순서

    while queue:
        # 큐의 맨 앞 문서가 가장 중요도가 높은지 확인
        if queue[0][0] == max(queue)[0]:
            order += 1  # 인쇄 순서 증가
            # 궁금한 문서가 인쇄되는 경우
            if queue[0][1] == index:
                return order
            else:
                queue.popleft() # 문서 인쇄
        else:
            # 현재 문서를 큐의 끝으로 이동
            queue.append(queue.popleft())

# T: 테스트 케이스 개수
T = int(sys.stdin.readline().strip())

for _ in range(T):
    # N: 문서 개수, M: 몇 번째로 인쇄되었는지 궁금한 문서
    N, M = map(int, sys.stdin.readline().strip().split())
    docs = sys.stdin.readline().strip().split()
    print(find_print_order(docs, M))
