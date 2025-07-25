import sys
from functools import cmp_to_key

input = sys.stdin.readline

# 문자열을 문자/숫자 덩어리 단위로 분리
def tokenize(word):
    tokens = []
    i = 0
    while i < len(word):
        if word[i].isdigit():
            j = i
            while j < len(word) and word[j].isdigit():
                j += 1
            tokens.append(word[i:j])  # 숫자 문자열 통째로 추가
            i = j
        else:
            tokens.append(word[i])
            i += 1
    return tokens

# 비교 함수
def compare(w1, w2):
    t1 = tokenize(w1)
    t2 = tokenize(w2)
    
    i = 0
    while i < min(len(t1), len(t2)):
        a, b = t1[i], t2[i]
        
        # 숫자 vs 문자: 숫자가 먼저
        if a.isdigit() and b.isalpha():
            return -1
        if a.isalpha() and b.isdigit():
            return 1
        
        # 둘 다 숫자일 때
        if a.isdigit() and b.isdigit():
            a_int = int(a)
            b_int = int(b)
            if a_int != b_int:
                return -1 if a_int < b_int else 1
            # 값 같으면 앞에 붙은 0 개수 적은 게 먼저
            a_zeros = len(a) - len(a.lstrip('0'))
            b_zeros = len(b) - len(b.lstrip('0'))
            if a_zeros != b_zeros:
                return -1 if a_zeros < b_zeros else 1

        # 둘 다 문자일 때
        if a.isalpha() and b.isalpha():
            if a.lower() != b.lower():
                return -1 if a.lower() < b.lower() else 1
            # 소문자 vs 대문자: 대문자가 먼저
            if a != b:
                return -1 if a < b else 1
        
        i += 1

    # 앞부분이 같으면 길이 짧은 게 먼저
    return -1 if len(t1) < len(t2) else 1

# 입력 및 출력
n = int(input())
words = [input().strip() for _ in range(n)]
words.sort(key=cmp_to_key(compare))

print(*words, sep='\n')
