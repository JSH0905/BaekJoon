### 덩치

### 덩치 = 키, 몸무게로 결정 -> (X,Y)
### 사람A = (x,y) , 사람B = (p,q) 일때  x > p 그리고 y > q 이라면 우리는 A의 덩치가 B의 덩치보다 "더 크다"
### 두 사람 C와 D의 덩치가 각각 (45, 181), (55, 173)이라면 몸무게는 D가 C보다 더 무겁고, 키는 C가 더 크므로, "덩치"로만 볼 때 C와 D는 누구도 상대방보다 더 크다고 말할 수 없다.

## 풀이 : 이중 for문

import sys

group = []

N = int(sys.stdin.readline())

for _ in range(N):
    group.append(list(map(int, sys.stdin.readline().split())))

for i in group:
    rank = 1

    for k in group:
        if i[0] < k[0] and i[1] < k[1]:
            rank += 1
    print(rank, end =" ")




