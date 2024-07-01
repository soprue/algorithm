import os

def sockMerchant(n, ar):
    answer = 0
    numbers = set(ar)
    
    for number in numbers:
        answer += ar.count(number) // 2
        
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
