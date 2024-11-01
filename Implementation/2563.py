# 색종이

## 풀이 방법
### 1. 문제에서 제시한 도화지를 2차원 배열로 나타낸다.(이때, 0으로 초기화)
### 2. 이중 for문을 통해서 색종이가 덮이는 부분은 1로 변경
### 3. 배열 내부의 1인 요소들을 합산함.
import sys


N = int(sys.stdin.readline())
drawing_paper = [[0] * 100 for _ in range(100)]

for _ in range(N):

    x, y = map(int, sys.stdin.readline().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            drawing_paper[i][j] = 1

area = 0
for k in range(100):
    area += drawing_paper[k].count(1)

print(area)
