# 단지 번호 붙이기

import sys
from collections import deque

N = int(sys.stdin.readline())

def bfs(start_x, start_y):
    queue = deque() # deque으로 bfs구현
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visited[nx][ny] == 0 and apt_complex[nx][ny] == "1":
                queue.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1

    return cnt


apt_complex = [list(str(sys.stdin.readline().strip())) for _ in range(N)] # 아파트 단지 생성
visited = [[0]*N for _ in range(N)] #방문 노드 확인용
apt_complex_sizes = []

# 이동방향 설정(가로, 세로로 지정)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if apt_complex[i][j] == "1" and visited[i][j] == 0:
            apt_complex_sizes.append(bfs(i, j))

apt_complex_sizes.sort()
print(len(apt_complex_sizes))
for size in apt_complex_sizes:
    print(size)