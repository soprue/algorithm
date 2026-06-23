import os

def jumpingOnClouds(c):
    current = 0
    jump = 0
    
    while current < len(c) - 1:
        if current + 2 < len(c) and c[current + 2] == 0:
            current += 2
        else:
            current += 1
        
        jump += 1
        
    return jump
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
