import sys
import math

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

N = int(sys.stdin.readline())
result = 0

for i in range(N, 1000001):
    if is_palindrome(i) and is_prime(i):
        result = i
        break

if result == 0: # 입력값이 만약 최대 값 100만일 경우
    result = 1003001 # 100만 이상이면서 팰림드롬 및 소수일 경우를 적용

print(result)
