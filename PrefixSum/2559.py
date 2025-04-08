# 2559번 수열

# 제한 시간 1초 = 1억번의 계산 이내로 끝내야함.

### 2번 풀이 방법 : 슬라이딩 윈도우 사용
### 사용 이융 : 고정된 범위 내에서 최댓값을 구해야하기 때문.

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))

sw_sum = sum(A[:k])
max_temp = sw_sum

for i in range(k, n):
    sw_sum = sw_sum - A[i-k] + A[i]
    max_temp = max(max_temp, sw_sum)

print(max_temp)


### 1번풀이 방법 
#### 문제 점 : 시간복잡도가 O(nxk) -> 위험함

# import sys

# input = sys.stdin.readline

# n, k = map(int, input().split())
# A = list(map(int, input().split()))

# max_temp = 0

# for i in range(n-k+1):
#     current_sum = sum(A[i:i+k])

#     if current_sum > max_temp:
#         max_temp = current_sum

# print(max_temp)