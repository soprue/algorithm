# https://www.acmicpc.net/problem/2108

import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
numbers.sort()

def mean(arr):
    print(round(sum(arr) / n))

def median(arr):
    print(arr[n // 2])
    
def mode(arr):
    # most_common() 메서드를 이용하여 출현 빈도가 높은 순으로 정렬
    count = Counter(arr).most_common()
    if len(count) > 1 and count[0][1] == count[1][1]:
        print(count[1][0])  # 두 번째로 작은 최빈값 출력
    else:
        print(count[0][0])
    
def calculate_range(arr):
    print(arr[-1] - arr[0]) # 정렬된 리스트이므로, 마지막 요소 - 첫 번째 요소

mean(numbers)
median(numbers)
mode(numbers)
calculate_range(numbers)
