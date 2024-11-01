### 크로아티아 알파벳

import sys

list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

def checkAlphabet(word):

    for i in list:
        word = word.replace(i, "*")

    print(len(word)-1)


word = sys.stdin.readline()
checkAlphabet(word)

