# https://www.acmicpc.net/problem/9375
import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    n = int(sys.stdin.readline().strip())

    closet = {}
    # 결과를 저장할 변수, 초기값은 1 (곱셈의 항등원)
    result = 1
    
    for _ in range(n):
        name, type = sys.stdin.readline().strip().split()

        if not type in closet:
            closet[type] = 1
        else:
            closet[type] += 1
    
    for i in closet:
        # 각 종류의 의상 개수에 1을 더한 값을 result에 곱함
        # 1을 더하는 이유: 만약 '모자' 종류의 옷이 2개 있다면, 이 '모자'를 입는 방법은 각각의 모자를 입는 2가지 방법과 모자를 전혀 안 쓰는 1가지 방법, 총 3가지 방법이 있기 때문임
        result *= (closet[i] + 1)

    # 모든 의상 종류에서 옷을 하나도 입지 않는 경우, 즉 전부 안 입는 경우가 포함되어 있기 때문에, 이를 제외하기 위해 최종적으로 1을 빼 줌
    print(result - 1)
