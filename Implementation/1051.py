#숫자 정사각형

import sys

n, m = map(int, sys.stdin.readline().split())
square = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)] # 초기 사각형 생성
max_len = min(n, m)

for len in range(max_len, 0, -1):
    for i in range(n - len + 1):
        for j in range(m - len + 1):
            if square[i][j] == square[i][j+len-1] == square[i+len-1][j] == square[i+len-1][j+len-1]:
                print(len**2)
                exit()

