import os

def lonelyinteger(a):
    answer = None
    numbers = set(a)
    
    for number in numbers:
        if(a.count(number) == 1):
            answer = number
            break
            
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
