#참외밭
#동 : 1 / 서 : 2 / 남 : 3 / 북 : 4
#인접한 변 알아내는법 : 리스트 안의 인덱스 사용

import sys

melons = int(sys.stdin.readline())
hexagon = [ list(map(int, sys.stdin.readline().split())) for _ in range(6) ]

max_width = 0; max_w_idx = 0
max_height = 0; max_h_idx = 0

for i in range(len(hexagon)):
    if hexagon[i][0] == 1 or hexagon[i][0] == 2:
        if max_width < hexagon[i][1]:
            max_width = hexagon[i][1]
            max_w_idx = i

    elif hexagon[i][0] == 3 or hexagon[i][0] == 4:
        if max_height < hexagon[i][1]:
            max_height = hexagon[i][1]
            max_h_idx = i

subW = abs(hexagon[(max_h_idx + 1) % 6][1] - hexagon[(max_h_idx - 1) % 6][1])
subH = abs(hexagon[(max_w_idx + 1) % 6][1] - hexagon[(max_w_idx - 1) % 6][1])

print(melons * (max_width * max_height - subW * subH))

