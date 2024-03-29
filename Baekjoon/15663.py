# https://www.acmicpc.net/problem/15663

from itertools import permutations

N, M = map(int, input().split())

nums = list(map(int, input().split()))
sequence = sorted(set(list(permutations(nums, M))))

for i in sequence:
  for j in i:
    print(j, end=" ")
  print()

# def generate_permutations(arr, M):
#     arr.sort()  # 입력 배열 정렬
#     result = []  # 결과 순열을 저장할 리스트
#     path = []  # 현재까지 선택된 숫자들을 저장할 리스트

#     def backtrack(available, path):
#         if len(path) == M:
#             result.append(tuple(path))  # 결과에 추가
#             return
#         for i in range(len(available)):
#             # 중복 숫자 건너뛰기
#             if i > 0 and available[i] == available[i-1]:
#                 continue
#             # 숫자 선택
#             backtrack(available[:i] + available[i+1:], path + [available[i]])

#     backtrack(arr, path)
#     return sorted(set(result))  # 중복 제거 후 정렬

# N, M = map(int, input().split())
# nums = list(map(int, input().split()))

# sequence = generate_permutations(nums, M)
# for i in sequence:
#   for j in i:
#     print(j, end=" ")
#   print()
