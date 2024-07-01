def miniMaxSum(arr):
    totalSum = sum(arr)
    minNum = min(arr)
    maxNum = max(arr)
    
    print(totalSum - maxNum, totalSum - minNum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
