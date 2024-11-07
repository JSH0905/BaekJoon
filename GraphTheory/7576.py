# 토마토

## -1 = 토마토 없음 / 0 = 익지 않은 토마토 / 1 = 익은 토마토

import sys
from collections import deque

def days_for_tomato():
    queue = deque()
    for i in range(N):
        for j in range(M):
            if storage[i][j] == 1:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        # 토마토가 익는 방향 설정
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<= nx < N and 0<= ny < M and storage[nx][ny] == 0:
                storage[nx][ny] = storage[x][y] + 1
                queue.append((nx, ny))

M, N = map(int, sys.stdin.readline().split())
storage = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
required_days = 0

#토마토 익히기
days_for_tomato()

#토마토 익히기 후 0 이 있으면 -1 반환
for row in storage:
    for i in row:
        if i == 0:
            print(-1)
            exit(0)
        else:
            required_days = max(required_days, i)

print(required_days-1)