# 11441 합 구하기 

# 문제 접근 방법 : 합배열을 통한 구간 합 구하기
# 합배열 알고리즘 선택 사유 : 데이터 수가 최대 10만개이므로 시간복잡도가 O(n^2)이면 위험하기 때문에
# 해당 접근 법의 시간 복잡도 : O(n+m)

import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

S = [0] * n # 합 배열 선언
S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]

answers = []

m = int(input())

for _ in range(m):
    answer = 0
    i, j = map(int, input().split())

    if i == 1:
        answer = S[j-1]
        answers.append(answer)

    elif i >= 2:
        answer = S[j-1] - S[i-2]
        answers.append(answer)


for answer in answers:
    print(answer)




