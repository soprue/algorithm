# https://www.acmicpc.net/problem/10282

import heapq
import sys
input = sys.stdin.readline

T = int(input())

def dijkstra(start, graph, n):
    # 각 컴퓨터까지의 최소 감염 시간을 저장
    min_time = [float('inf')] * (n + 1)
    min_time[start] = 0  # 시작 컴퓨터는 감염 시간이 0
    
    # 우선순위 큐를 사용하여 가장 빠른 감염 시간을 우선적으로 처리
    queue = [(0, start)]  # (감염 시간, 컴퓨터 번호)

    while queue:
        # 큐에서 감염 시간이 가장 짧은 컴퓨터를 추출
        current_time, current_computer = heapq.heappop(queue)

        # 현재 큐에서 가져온 시간이 이미 기록된 감염 시간보다 길 경우 무시
        if current_time > min_time[current_computer]: continue

        for next_computer, time in graph[current_computer]:
            next_time = current_time + time
            if next_time < min_time[next_computer]:
                min_time[next_computer] = next_time
                heapq.heappush(queue, (next_time, next_computer))

    # 모든 컴퓨터를 순회하면서 감염된 컴퓨터의 수와 마지막 컴퓨터가 감염될 때까지의 시간을 계산
    count = 0
    max_time = 0
    for time in min_time:
        if time != float('inf'):  # 감염되었다면
            count += 1
            if time > max_time:  # 가장 늦게 감염된 시간 업데이트
                max_time = time

    return count, max_time

for _ in range(T):
    # n: 컴퓨터 개수, d: 의존성 개수, c: 해킹당한 컴퓨터 번호
    n, d, c = map(int, input().strip().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        # a가 b를 의존하며, b가 감염되면 s초 후 a도 감염
        a, b, s = map(int, input().strip().split())
        graph[b].append((a, s))

    count, max_time = dijkstra(c, graph, n)
    print(count, max_time)
