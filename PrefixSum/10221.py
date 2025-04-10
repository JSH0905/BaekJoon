# 10221번 Maximum Subarray

# 접근 방법 : 투 포인터? -> 비효율 
# 개선 방법 : 카데인 알고리즘

import sys

input = sys.stdin.readline

t = int(input())
answers = [] 

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    max_sum = current_sum = A[0]

    for a in A[1:]:
        current_sum = max(a, current_sum + a)
        max_sum = max(max_sum, current_sum)

    answers.append(max_sum)

for answer in answers:
    print(answer)