### 1차 문제 풀이 방법 : 합배열 이용 
#### 문제 : 이중 for문으로 인한 시간복잡도(= O(n^2) )가 높아져 시간초과 문제 발생

# import sys

# input = sys.stdin.readline
# answer = 0

# n, m = map(int, input().split())
# A = list(map(int, input().split()))

# S = [0] * n
# S[0] = A[0]

# for i in range(1, n):
#     S[i] = S[i-1] + A[i]

# for prefixSum in S:
#     if prefixSum == m:
#         answer += 1


# for i in range(n):
#     for j in range(n):
#         if S[j] - S[i] == m:
#             answer += 1

# print(answer)

### 2차 해결방법 
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

start, end, answer = 0, 0, 0

while end < n:
    current_sum = sum(A[start:end+1])
    
    if current_sum == m:
        answer += 1
        end += 1
    
    elif current_sum > m:
        start += 1
    
    else:
        end += 1

print(answer)
