# 유기농 배추

import sys
from collections import deque

def calc_required_earthworms(start_x, start_y):
    queue = deque([(start_x, start_y)])

    while queue:
        a,b = queue.popleft()

        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            if 0 <= nx < N and 0 <= ny < M and cabbage_patch[nx][ny] == 1:
                queue.append((nx, ny))
                cabbage_patch[nx][ny] = 0

    return 1


T = int(sys.stdin.readline()) # 테스트 케이스 수
cnt_required_earthworms = []

for _ in range(T):

    M, N, K = map(int, sys.stdin.readline().split()) # M = 가로, N = 세로, K = 배추 수
    cabbage_patch = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split()) # x좌표, y 좌표
        cabbage_patch[y][x] = 1 # 배추밭 생성완료

    # 지렁이 이동방향 설정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if cabbage_patch[i][j] == 1:
                cnt += calc_required_earthworms(i, j)

    cnt_required_earthworms.append(cnt)

for count in cnt_required_earthworms:
    print(count)

