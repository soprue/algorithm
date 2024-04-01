# https://www.acmicpc.net/problem/17140

import sys

def operation(arr):
    # 배열에 어떤 연산을 적용해야 하는지 결정
    if len(arr) >= len(arr[0]):
        return r_operation(arr)
    else:
        return c_operation(arr)

def r_operation(arr):
    new_arr = []
    max_length = 0 

    for row in arr:
        count = {}
        for num in row:
            if num != 0:
                count[num] = count.get(num, 0) + 1

        # 등장 횟수와 숫자를 기준으로 정렬
        sorted_row = sorted(count.items(), key=lambda x: (x[1], x[0]))

        # 정렬된 결과에 대해 숫자와 등장 횟수를 차례대로 추가
        new_row = []
        for num, freq in sorted_row:
            new_row += [num, freq]

        max_length = max(max_length, len(new_row))
        new_arr.append(new_row)
        
    # 모든 행이 같은 길이를 가지도록 0으로 채움
    for row in new_arr:
        row.extend([0] * (max_length - len(row)))
        
    return new_arr

def c_operation(arr):
    # 배열을 전치 (행과 열 바꾸기)
    transposed = list(zip(*arr))
    # 전치된 배열에 R 연산 적용
    operated = r_operation(transposed)
    # 다시 전치하여 원래 배열 형태로 복구
    return [list(row) for row in zip(*operated)]

def find_time_to_k(r, c, k, arr):
    time = 0

    while time <= 100:
        if r <= len(arr) and c <= len(arr[0]) and arr[r-1][c-1] == k:
            return time
        else:
            arr = operation(arr)
            time += 1
        
    return -1

r, c, k = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

print(find_time_to_k(r, c, k, A))
