# https://www.acmicpc.net/problem/17413

def reverse_words(s):
    i, n = 0, len(s)
    result = []

    while i < n:
        if s[i] == '<':  # 태그 시작
            # 태그 끝 찾기
            j = i
            while s[j] != '>':
                j += 1

            # 태그 전체를 결과에 추가
            result.append(s[i:j+1])
            i = j + 1  # 태그 다음 위치로 인덱스 이동
        elif s[i] == ' ':  # 공백
            result.append(' ')
            i += 1
        else:
            # 단어 끝 찾기
            j = i
            while j < n and s[j] not in '< >':
                j += 1

            # 단어를 뒤집어서 결과에 추가
            result.append(s[i:j][::-1])
            i = j  # 단어 다음 위치로 인덱스 이동

    return ''.join(result)

s = input().strip()
print(reverse_words(s))
