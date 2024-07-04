from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # 다리의 길이만큼 0으로 초기화
    bridge_weight = 0  # 다리 위의 현재 총 무게
    truck_weights = deque(truck_weights)  # 대기 트럭
    
    while bridge:
        time += 1
        bridge_weight -= bridge.popleft() # 다리에서 트럭이 빠져 나감
        
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight: # 새 트럭이 다리에 올라갈 수 있는 경우
                truck = truck_weights.popleft()
                bridge.append(truck)
                bridge_weight += truck
            else:
                bridge.append(0) # 다리에 트럭이 진입하지 못하는 경우
    
    return time
