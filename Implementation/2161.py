#카드 1

import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()
result = []

for i in range(1, N+1):
    q.append(i)

while q:
    result.append(q.popleft())

    if len(q) > 0:
        q.append(q.popleft())

print(*result)