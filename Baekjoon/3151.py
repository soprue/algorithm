import sys

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().strip().split()))
A.sort()

answer = 0

# 첫 번째 학생(A[i])를 하나 고정
# -> 남은 학생들 중에서 두 명을 골라 합이 -A[i]인 쌍을 찾음
# -> 이렇게 하면 "3명 합 = 0" 이 "2명 합 = 특정 숫자" 문제로 
# 이 두 명을 찾을 때 투포인터라는 방법을 쓰면 빠름
for i in range(N - 2):
    target = -A[i]
    left = i + 1
    right = N - 1
    
    while left < right:
        total = A[left] + A[right]
        
        if total < target:
            left += 1
        elif total > target:
            right -= 1
        else: # A[left] + A[right] == target
            # 같은 값이 여러 개일 경우 처리
            if A[left] == A[right]:
                # left~right까지 전부 같은 값 → 조합 개수 추가
                n = right - left + 1
                answer += n * (n - 1) // 2
                break
            else:
                # 왼쪽 값이 몇 개 연속인지 세기
                l_count = 1
                while left + l_count < right and A[left + l_count] == A[left]:
                    l_count += 1
                
                # 오른쪽 값이 몇 개 연속인지 세기
                r_count = 1
                while right - r_count > left and A[right - r_count] == A[right]:
                    r_count += 1
                    
                # 경우의 수 더하기
                answer += l_count * r_count
                # 포인터 이동
                left += l_count
                right -= r_count
                    
                    
print(answer)
