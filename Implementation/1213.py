#팰린드롬 만들기

import sys
from collections import Counter

def canBePalindrome(str):
    freq = Counter(str)
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    
    return odd_count <= 1

def makePalindrome(str):
    freq = Counter(str)
    odd_char = None
    left = []
    for char in sorted(freq.keys()):
        count = freq[char]
        if count % 2 == 1:
            if odd_char == None:
                odd_char = char
                count -= 1
        
        left.extend(char * (count // 2))

        left_part = ''.join(left)
        middle_part = odd_char if odd_char else ''
        right_part = left_part[::-1]

    print(left_part + middle_part + right_part)


name = sys.stdin.readline().strip()

if canBePalindrome(name) == False:
    print("I'm Sorry Hansoo")

else:
    makePalindrome(name)