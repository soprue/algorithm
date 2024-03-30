# https://www.acmicpc.net/problem/28432

import sys

# 입력 한번에 읽기
input_lines = sys.stdin.readlines()

N = int(input_lines[0].strip())
records = [line.strip() for line in input_lines[1:N + 1]]

question_index = records.index("?")
prev_char = records[question_index - 1][-1] if question_index > 0 else None
next_char = records[question_index + 1][0] if question_index + 1 < N else None

record_set = set(records)

M = int(input_lines[N + 1].strip())
candidates = [line.strip() for line in input_lines[N + 2:]] 

for word in candidates:
    word = word.strip() 
    
    if word in record_set:
        continue

    # prev_char이 None이라면 '?'가 첫 단어이므로 앞 문자 조건은 무시됨
    # next_char이 None이라면 '?'가 마지막 단어이므로 뒤 문자 조건은 무시됨
    # prev_char, next_char 둘 다 None이 아니라면, 해당 문자와 일치해야 함
    if (prev_char is None or word[0] == prev_char) and (next_char is None or word[-1] == next_char):
        print(word)
        break
