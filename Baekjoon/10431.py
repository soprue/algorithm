P = int(input())

for _ in range(P):
    arr = list(map(int, input().split()))
    test_case_number = arr[0]
    heights = arr[1:]

    total_steps = 0
    
    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            if heights[i] > heights[j]:
                heights[i], heights[j] = heights[j], heights[i]
                total_steps += 1
                
    print(test_case_number, total_steps)
