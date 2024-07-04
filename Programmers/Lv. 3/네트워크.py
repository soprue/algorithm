def solution(n, computers):
    def DFS(node, visited, computers):
        stack = [node]
        while stack:
            v = stack.pop()
            if not visited[v]:
                visited[v] = True
                for i in range(n):
                    if computers[v][i] == 1 and not visited[i]:
                        stack.append(i)
    
    count = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            DFS(i, visited, computers)
            count += 1
            
    return count
