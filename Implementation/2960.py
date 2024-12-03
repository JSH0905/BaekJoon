# 에라토스테네스의 체

# 규칙
## 1. 2 ~ N까지의 모든 정수를 적음
## 2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다 = P, 이 수는 소수
## 3. P를 지우고 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
## 4. 아직 모든 수를 지우지 않았다면 다시 2번단계로 이동.

import sys

N, K = map(int, sys.stdin.readline().split())

arr = list(range(2, N+1))
result = []

for num in arr[:]:
    if num in arr:
        multiplies = [x for x in arr if x % num == 0]
        result.extend(multiplies)
        arr = [x for x in arr if x % num != 0]

print(result[K-1])

    


