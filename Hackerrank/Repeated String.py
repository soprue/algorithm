import os

def repeatedString(s, n):
    full_repeat = n // len(s) 
    remain = n % len(s)
    
    a_count_in_s = s.count('a')
    a_count_in_remain = s[:remain].count('a')
    
    return a_count_in_s * full_repeat + a_count_in_remain
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
