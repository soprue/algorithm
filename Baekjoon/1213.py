# https://www.acmicpc.net/problem/1213

import collections

def create_palindrome(name):
    alphabet = collections.Counter(name)
    mid = ''
    result = ''

    odd_count = sum(v % 2 for v in alphabet.values())
    if odd_count >= 2:  # 홀수가 2개 이상이면 팰린드롬 불가능
        return "I'm Sorry Hansoo"

    for char, num in sorted(alphabet.items()):
        if num % 2 == 1:
            mid = char
        result += char * (num // 2) 

    return result + mid + result[::-1]

name = input()
print(create_palindrome(name))
