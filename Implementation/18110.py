# solved.ac
# 절사평균 : 가장 큰 값들과 가장 작은 값들을 제외하고 평균을 내는 것.

# 틀린 이유 : round의 오사오입(파이썬의 경우) -> 직접 새로운 round를 정의해줌.

import sys
from collections import deque

def new_round(val):
    if val - int(val) >= 0.5:
        return int(val)+1
    else:
        return int(val)

op = []
q = deque()
n = int(sys.stdin.readline())
sum = 0
level = 0

ex = new_round(n * 15 / 100)

for _ in range(n):
    op.append(int(sys.stdin.readline()))

q.extend(sorted(op))

for _ in range(ex):
    q.popleft()
    q.pop()

for score in q:
    sum += score

if n != 0:
    level = new_round(sum / len(q))

print(level)