import os

def timeConversion(s):
    time = s[:-2]
    timePeriod = s[-2:]
    
    h, m, s = map(int, time.split(":"))
    
    if timePeriod == "PM" and h != 12:
        h += 12
    elif timePeriod == "AM" and h == 12:
        h = 0
        
    time = f"{h:02}:{m:02}:{s:02}"
    
    return time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()
