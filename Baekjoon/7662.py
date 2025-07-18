import sys
import heapq

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    k = int(input().strip())
    min_heap = []
    max_heap = []
    visited = [False] * k
    
    for i in range(k):
        cmd, n = input().strip().split()
        n = int(n)
        
        if cmd == "I":
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (-n, i))
            visited[i] = True # 아직 삭제 안 됨
        else:
            if n == 1: # 최댓값 삭제
                # max_heap의 top이 삭제된 값이면 무시하고 제거
                while max_heap and not visited[max_heap[0][1]]: 
                    heapq.heappop(max_heap) 
                if max_heap:
                    # top이 아직 유효하면 → 삭제 표시하고 pop
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else: # 최솟값 삭제
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
          
    # 힙 top에 삭제된 값이 남아 있을 수 있으니 정리          
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
        
    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
