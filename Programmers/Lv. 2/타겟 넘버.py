def solution(numbers, target):
    answer = 0
    
    def DFS(level, sum):
        nonlocal answer 
        
        if level == len(numbers):
            if sum == target:
                answer += 1
        else:
            DFS(level + 1, sum + numbers[level])
            DFS(level + 1, sum - numbers[level])
        
    DFS(0, 0)
    return answer
