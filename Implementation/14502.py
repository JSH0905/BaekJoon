# 연구소

import sys
import copy
from itertools import combinations
from collections import deque

def leak_virus(lab_copy):
    q = deque() # bfs

    for i in range(n):
        for j in range(m):
            if lab_copy[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and lab_copy[nx][ny] == 0:
                lab_copy[nx][ny] = 2
                q.append((nx, ny))

    global safe
    cnt = sum([i.count(0) for i in lab_copy])
    safe = max(safe, cnt)

n, m = map(int, sys.stdin.readline().split()) # n = 세로, m = 가로

lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 연구소 생성
candidate = [(x,y) for x in range(m) for y in range(n) if lab[y][x] == 0]
safe = 0

# 바이러스 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for c in combinations(candidate, 3):
    lab_copy = copy.deepcopy(lab)
    for x, y in c:
        lab_copy[y][x] = 1
    leak_virus(lab_copy)

print(safe)