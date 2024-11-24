# 단어 뒤집기2

import sys
from collections import deque

string = list(sys.stdin.readline().strip()) # 문자열
deque = deque()
check = False

for character in string:

    if character == "<":
        check = True
        while deque:
            print(deque.pop(), end='')
        deque.append(character)

    elif character == ">" and check == True:
        while deque:
            print(deque.popleft(), end='')
        print(character, end='')
        check = False

    elif character == " " and check == False:
        while deque:
            print(deque.pop(), end='')
        print(character, end='')

    else:
        deque.append(character)


while deque:
    print(deque.pop(), end='')