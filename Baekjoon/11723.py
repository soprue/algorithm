# https://www.acmicpc.net/problem/11723

import sys

N = int(sys.stdin.readline().strip())

S = set()

for _ in range(N) :
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()

    else :
        operation, number = temp[0], temp[1]
        number = int(number)

        if operation == "add" :
            S.add(number)
        elif operation == "remove" :
            S.discard(number)
        elif operation == "check" :
            print("1" if number in S else "0")
        elif operation == "toggle" :
            if number in S :
                S.discard(number)
            else :
                S.add(number)
