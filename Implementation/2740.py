#행렬 곱셈

import sys

N, M = map(int, sys.stdin.readline().split())
A = [ list(map(int, sys.stdin.readline().split())) for _ in range(N)]
M, K = map(int, sys.stdin.readline().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

result = [[0]*K for _ in range(N)]

for row in range(N):
    for col in range(K):
        element = 0
        for i in range(M):
            element += A[row][i] * B[i][col]
        result[row][col] = element

for i in result:
    print(*i)