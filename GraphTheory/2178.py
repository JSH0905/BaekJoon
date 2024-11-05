#미로 탐색
## 최단 거리 찾기에는 BFS 사용이 유리함.

import sys
from collections import deque # BFS 구현시 덱 사용  / 리스트 사용보다 효율성 부분에서 유리함.

def escape_from_maze():
    queue = deque()
    queue.append( (0,0) ) # 시작 지점 큐에 추가
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if visited[nx][ny]==False and maze[nx][ny]=="1":
                queue.append( (nx,ny) )
                visited[nx][ny]=True
                distance[nx][ny] += distance [x][y]

N,M = map(int, sys.stdin.readline().split())

maze = [ list(str(sys.stdin.readline().strip())) for _ in range(N) ] # 미로 생성

visited = [[False for _ in range(M)] for i in range(N)] # BFS에서 방문한 노드 담는 역할
distance = [[1 for _ in range(M)] for i in range(N)] # BFS 결과로 나온 이동거리들을 담는 역할

dx = [ -1, 1, 0, 0 ] # 세로 이동방향 설정
dy = [ 0, 0, -1, 1 ] # 가로 이동방향 설정

escape_from_maze()
print(distance[N-1][M-1])