import os

def sockMerchant(n, ar):
    count = {}
    
    for color in ar:
        if color in count:
            count[color] += 1
        else:
            count[color] = 1
    
    answer = 0
    
    for value in count.values():
        answer += value // 2
        
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
