# https://www.acmicpc.net/problem/5525

N = int(input().strip())
M = int(input().strip())
S = input().strip()

cursor, count, result = 0, 0, 0

while cursor < (M - 1):
    if S[cursor:cursor + 3] == 'IOI':
        count += 1
        cursor += 2
        if count == N:
            result += 1
            count -= 1  # 다음 "IOI" 패턴 검색을 위해 재활용
    else:
        cursor += 1
        count = 0

print(result)

# https://aia1235.tistory.com/30 참고함
