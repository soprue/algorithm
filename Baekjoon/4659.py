import sys
input = sys.stdin.readline

vowels = ['a', 'e', 'i', 'o', 'u']

def is_acceptable(word):
    vowels = 'aeiou'
    include_vowel = any(char in vowels for char in word)
    vowel_count = 0
    consonant_count = 0
    prev_char = ''

    for _, char in enumerate(word):
        if char == prev_char and char not in 'eo':
            return False
        
        if char in vowels:
            vowel_count += 1
            consonant_count = 0
        else:
            consonant_count += 1
            vowel_count = 0
        
        if vowel_count == 3 or consonant_count == 3:
            return False

        prev_char = char

    return include_vowel

while True:
    word = input().strip()
    if word == 'end':
        break

    result = 'acceptable.' if is_acceptable(word) else 'not acceptable.'
    print(f'<{word}> is {result}')
