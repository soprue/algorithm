import math

def solution(progresses, speeds):
    answer = []
    stack = [math.ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)]
        
    currentDeployDay = stack[0]
    deployCount = 1
    
    for endDay in stack[1:]:
        if currentDeployDay >= endDay:
            deployCount += 1
        else:
            answer.append(deployCount)
            currentDeployDay = endDay
            deployCount = 1
            
    answer.append(deployCount)
              
    return answer
