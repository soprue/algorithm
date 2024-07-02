from functools import cmp_to_key

def compare(x, y):
    if x + y < y + x:
        return 1
    else:
        return -1

def solution(numbers):
    strings = list(map(str, numbers))
    strings = sorted(strings, key=cmp_to_key(compare))
    answer = ''.join(strings)
    return answer if answer[0] != '0' else '0'
