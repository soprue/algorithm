# https://www.acmicpc.net/problem/25206

import sys

rating = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

total_credit = 0 # 학점 총합을 담을 변수
total_score = 0	# (학점 * 과목평점) 총합을 담을 변수

for _ in range(20) :
    _, credit, grade = list(sys.stdin.readline().split())
    credit = float(credit)
    if grade != "P" :
        total_credit += credit
        total_score += credit * rating[grade]

print(format(total_score / total_credit, ".6f"))
