import os

def diagonalDifference(arr):
    n = len(arr)
    leftToRight = 0
    rightToLeft = 0
    
    for i in range(n):
        leftToRight += arr[i][i]
        rightToLeft += arr[i][n - 1 - i]
        
    return abs(leftToRight - rightToLeft)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')
    fptr.close()
