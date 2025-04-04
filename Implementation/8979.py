# 올림픽 

import sys

N, K = map(int, sys.stdin.readline().split())

nation = [ list(map(int, sys.stdin.readline().split())) for _ in range(N)]
nation.sort(key= lambda x : (x[1], x[2], x[3]), reverse= True)
idx = [nation[i][0] for i in range(N)].index(K)

for i in range(N):
    if nation[idx][1:] == nation[i][1:]:
        print(i + 1)
        break

