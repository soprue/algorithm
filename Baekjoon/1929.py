# https://www.acmicpc.net/problem/1929

from math import sqrt

m, n = map(int, input().strip().split())

# 소수 판별을 위한 배열 초기화, 모두 True로 설정
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

# 에라토스테네스의 체 알고리즘 적용
for i in range(2, int(sqrt(n)) + 1):
    if is_prime[i]:  # i가 소수인 경우 i의 배수들을 소수가 아님으로 표시
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

# M부터 N까지 소수 출력
for i in range(m, n + 1):
    if is_prime[i]:
        print(i)
