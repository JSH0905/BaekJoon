#스위치 켜고 끄기

import sys

switch = int(sys.stdin.readline()) 
status = list(map(int, sys.stdin.readline().split()))
students = int(sys.stdin.readline())

for _ in range(students):
    sex, num = map(int, sys.stdin.readline().split())

    if(sex == 1):
        for i in range(1, len(status)+1):
            if i % num == 0:
                status[i-1] = 1 - status[i-1]
            
            else:
                pass
        
    elif(sex == 2):
        
        pivot = num - 1
        left, right = pivot, pivot

        while left > 0 and right < switch - 1:
            if status[left - 1] == status[right + 1]:
                left -= 1
                right += 1
            else:
                break

        for i in range(left, right + 1):
            status[i] = 1 - status[i]

    else:
        exit()

for i in range(0, len(status), 20):
     print(" ".join(map(str, status[i:i+20])))