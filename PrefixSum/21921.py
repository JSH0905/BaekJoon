# 21921번 블로그

# 문제 접근 방법 : 슬라이딩 윈도우

import sys

input = sys.stdin.readline

n, x = map(int, input().split())
A = list(map(int, input().split()))

sw_sum = sum(A[:x])
max_visitor = sw_sum
period_cnt = 1

for i in range(x, n):
    sw_sum = sw_sum - A[i-x] + A[i]
    
    if sw_sum == max_visitor:
        period_cnt += 1

    elif sw_sum > max_visitor:
        max_visitor = sw_sum
        period_cnt = 1
    
if max_visitor == 0:
    print("SAD")
else:
    print(max_visitor)
    print(period_cnt)
