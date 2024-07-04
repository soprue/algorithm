def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    
    for i in range(n):
        if citations[i] <= i:
            return i
        
    return n
