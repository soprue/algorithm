import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

recommends = list(map(int, input().split()))
frame = [] # 사진틀 (학생 번호 저장)
info = {} # { 학생 번호: [추천 수, 등록 순서] }

order = 0
for student in recommends:
    if student in info:
        info[student][0] += 1
    else:
        if len(frame) == N:
            remove = min(frame, key=lambda x: (info[x][0], info[x][1]))
            frame.remove(remove)
            del info[remove]
        
        frame.append(student)
        info[student] = [1, order]
    order += 1

frame.sort()

print(' '.join(map(str, frame)))
