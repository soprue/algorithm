# https://www.acmicpc.net/problem/1924

import sys 

input_month, input_day = map(int, sys.stdin.readline().split())

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekdays = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

total_days = sum(month_days[:input_month - 1]) + input_day

print(weekdays[total_days % 7])
