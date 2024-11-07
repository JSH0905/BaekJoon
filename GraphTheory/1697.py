# 숨바꼭질
## n = 수빈이 / k = 동생
### 이동 방향 | 걷기 : 좌/우 1칸 | 순간이동 : 현 위치 2배

import sys
from collections import deque

def hide_and_seek():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            print(point[x])
            break
        for i in (x-1, x+1, x*2):
            if 0 <= i <= 100000 and point[i] == 0:
                point[i] = point[x] + 1
                q.append(i)


point = [0] * 100001  # 점 생성
n, k = map(int, sys.stdin.readline().split())

hide_and_seek()