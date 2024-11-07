# 연결 요소의 개수

import sys
from collections import deque

def bfs(start, graph, visited) :
    q = deque([start])
    visited[start] = 1

    while q :
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0 :
                q.append(i)
                visited[i] = 1

n, m = map(int,sys.stdin.readline().split()) # n = 정점 개수 , m = 간선 개수

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for _ in range(m):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    if visited[i] == 0:
        bfs(i, graph, visited)
        cnt += 1

print(cnt)