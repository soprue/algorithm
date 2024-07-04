import os

def countingValleys(steps, path):
    count = 0
    current = 0
    
    for val in path:
        if val == "U":
            if current == -1:
                count += 1
            current += 1
        elif val == "D":
            current -= 1
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())
    path = input()

    result = countingValleys(steps, path)
    fptr.write(str(result) + '\n')
    fptr.close()
