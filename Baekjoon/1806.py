# https://www.acmicpc.net/problem/1806

# 투 포인터 기법: 주어진 배열에서 두 개의 포인터를 이용해 문제의 조건을 만족하는 부분 배열을 찾는 알고리즘
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

start, end = 0, 0
sum = 0 # 합을 저장할 변수
min_length = sys.maxsize # 먼저 최대 길이로 지정

while True:
    if sum >= S:
        min_length = min(min_length, end - start)  # 최소 길이 갱신
        sum -= numbers[start]  # 시작 포인터가 가리키는 값을 빼고 오른쪽으로 이동
        start += 1
    elif end == N: # 끝 포인터가 배열 끝에 도달하면 break
        break
    else:
        sum += numbers[end] # 끝 포인터가 가리키는 값을 더하고 오른쪽으로 이동
        end += 1

# 만일 그러한 합을 만드는 것이 불가능하면 0 출력
if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)
