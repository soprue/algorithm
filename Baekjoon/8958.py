# https://www.acmicpc.net/problem/8958

n = int(input())

for _ in range(n):
    input_str = input().strip()

    total_score, count = 0, 0 
    for char in input_str:
        if char == "O":
            count += 1
            total_score += count
        else:
            count = 0
    print(total_score)
