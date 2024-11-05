# 바이러스

import sys
from collections import deque

def bfs():
    cnt = 0

    queue = deque()
    queue.append(1)
    bfs_visited[1] = True
    while queue:
        infected_com = queue.popleft()
        for i in graph[infected_com]:
            if bfs_visited[i] == False:
                bfs_visited[i] = True
                queue.append(i)
                cnt += 1

    print(cnt)


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1) ]
bfs_visited = [False for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향으로 만들기


bfs()

