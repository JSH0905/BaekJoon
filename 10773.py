### 제로

### 풀이 1번 : list 사용. 이유 : 스택이라고 판단.

import sys

K = int(sys.stdin.readline())

sum_list = []
result = 0

for i in range(K):
    num = int(sys.stdin.readline())
    if num != 0:
        sum_list.append(num)
    else:
        sum_list.pop()

for element in sum_list:
    result += element

print(result)


