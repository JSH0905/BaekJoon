# 구간 합 구하기 4

import sys

input = sys.stdin.readline

answers = []

n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * (n+1)

for i in range(1, n+1):
    S[i] = S[i-1] + A[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    result = S[j] - S[i-1]
    answers.append(result)

for answer in answers:
    print(answer)