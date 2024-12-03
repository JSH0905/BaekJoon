# 마인크래프트

import sys

# 지형 생성
N, M, B = map(int, sys.stdin.readline().split())

ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = sys.maxsize
idx = 0


# 한 블럭마다 높이 256까지 순회
for floor in range(257):
    exceed_block, lack_block = 0, 0

    for i in range(N):
        for j in range(M):
            if ground[i][j] > floor:
                exceed_block += ground[i][j] - floor
            else:
                lack_block += floor - ground[i][j]

    if exceed_block + B >= lack_block:
        if(exceed_block * 2) + lack_block <= answer:
            answer = (exceed_block * 2) + lack_block
            idx = floor

print(answer, idx)   