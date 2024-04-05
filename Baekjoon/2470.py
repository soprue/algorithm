# https://www.acmicpc.net/problem/2470

N = int(input())
solutions = list(map(int, input().split()))

# 용액을 오름차순으로 정렬
solutions.sort()

# 양 끝에서 시작하는 두 포인터를 설정
left = 0  # 가장 왼쪽(가장 작은 값)
right = N - 1  # 가장 오른쪽(가장 큰 값)
# 현재 가장 가까운 합을 초기값으로 설정
closest_sum = solutions[left] + solutions[right]
# 가장 0에 가까운 두 용액의 특성값을 저장할 튜플
closest_pair = (solutions[left], solutions[right])

while left < right:
    # 현재 포인터들이 가리키는 두 용액의 합 계산
    current_sum = solutions[left] + solutions[right]
    
    # 현재 합이 더 0에 가까우면 업데이트
    if abs(current_sum) < abs(closest_sum):
        closest_sum = current_sum
        closest_pair = (solutions[left], solutions[right])
    
    if current_sum < 0:
        left += 1
    elif current_sum > 0:
        right -= 1
    else:  # 정확히 0이면 가장 가까운 값이므로 반복을 종료
        break

print(closest_pair[0], closest_pair[1])
