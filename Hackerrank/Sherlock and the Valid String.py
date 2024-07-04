
import os
from collections import Counter

def isValid(s):
    counter = Counter(s)
    frequencies = list(counter.values())
    freq_counter = Counter(frequencies)
    
    print(freq_counter)
    
    if len(freq_counter) == 1:
        return "YES"
    if len(freq_counter) > 2:
        return "NO"
        
    min_freq = min(freq_counter.keys())
    max_freq = max(freq_counter.keys())
    
    if freq_counter[min_freq] == 1 and min_freq == 1:
        return "YES"
    if freq_counter[max_freq] == 1 and max_freq - min_freq == 1:
        return "YES"
        
    return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')
    fptr.close()
