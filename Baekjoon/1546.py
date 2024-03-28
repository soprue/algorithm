# https://www.acmicpc.net/problem/1546

N = int(input())
grades = list(map(int, input().split()))
M = max(grades)

for i in range(N) :
    grades[i] = grades[i] / M * 100

print(sum(grades) / N)
