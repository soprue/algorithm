import os
from collections import defaultdict, deque

def roadsAndLibraries(n, c_lib, c_road, cities):
    # 도로 건설 비용이 도서관 건설 비용보다 크거나 같은 경우, 모든 도시에 도서관을 건설하는 것이 최소 비용
    if c_lib <= c_road:
        return n * c_lib
    
    # 주어진 도시 연결 정보를 바탕으로 양방향 그래프 생성
    graph = defaultdict(list)
    for u, v in cities:
        graph[u].append(v)
        graph[v].append(u)
        
    visited = [False for _ in range(n + 1)]
    def bfs(start):
        queue = deque([start])
        count = 0
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    count += 1
        return count

    # 최소 비용 계산 (하나의 도서관과 여러 도로)
    total_cost = 0
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            size = bfs(i)
            total_cost += c_lib + size * c_road
        
    return total_cost
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])
        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)
        fptr.write(str(result) + '\n')

    fptr.close()
