import sys

N = int(sys.stdin.readline())
num = N
result = 1

def cycle(num):
    if num < 10:
        num = '0' + str(num)
    else:
        num = str(num)
    
    num = str(num[1]) + str(int(num[0]) + int(num[1]))[-1]
    return int(num)

while True:
    num = cycle(num)
    if num == N:
        print(result)
        break
    result += 1
