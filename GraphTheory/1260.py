# DFS 와 BFS
## BFS, DFS 구현시 덱 사용이 유리 / BFS = 큐, DFS = 스택 구조

import sys


def dfs(V):
    dfs_visited[V] = 1 # 방문처리
    print(V, end = ' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and dfs_visited[i] == 0:
            dfs(i)

def bfs(V):
    queue = [V]
    bfs_visited[V] = 1 # 방문처리
    while queue:
        V = queue.pop(0)
        print(V, end =' ')
        for i in range(1, N+1):
            if graph[V][i] == 1 and bfs_visited[i] == 0:
                queue.append(i)
                bfs_visited[i] = 1


N, K, V = map(int, sys.stdin.readline().split())

graph = [[0]*(N+1) for _ in range(N+1)] # 리스트 컴프리핸션

for i in range(K):
    a,b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

dfs_visited = [0] * (N+1)
bfs_visited = dfs_visited.copy()


dfs(V)
print()
bfs(V)
