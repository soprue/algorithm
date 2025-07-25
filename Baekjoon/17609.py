import sys

input = sys.stdin.readline

T = int(input().strip())

def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

for _ in range(T):
    s = input().strip()
    left = 0
    right = len(s) - 1
    result = 0
    
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1):
                result = 1
            else:
                result = 2
            break
    
    print(result)
