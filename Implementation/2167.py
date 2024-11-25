# 2차원 배열의 합

# 문제 풀이 방법 : 누적합 사용

import sys

N, M = map(int, sys.stdin.readline().split())
arr = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]
prefix_sum = [[0] * (M+1) for _ in range(N+1)] # 누적합 배열 초기

for i in range(1, N+1):
    for j in range(1, M+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + arr[i-1][j-1]

K = int(sys.stdin.readline())

for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    result = prefix_sum[x][y] - prefix_sum[x][j-1] - prefix_sum[i-1][y] + prefix_sum[i-1][j-1]
    print(result)



