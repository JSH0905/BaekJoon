#사탕 게임

#내가 생각한 방법
## 1. 원본 리스트를 복사하여 복사본을 만든다.(원본 리스트 변경하지 않도록)
## 2. 인접한 요소(상하, 좌우)가 서로 다른지 확인한 후 교환
## 3. 교환 이후 복사본의 행, 열을 조사하여 연속된 문자열 수의 최대값을 answer리스트에 담음
## 4. answer 리스트의 최대값을 출력

import sys
from copy import deepcopy

N = int(sys.stdin.readline())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]
answer = []

def check_max_count(temp_board):
    max_count = 0
    for row in temp_board:
        count = 1
        for k in range(1, N):
            if row[k] == row[k-1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
    
    for col in range(N):
        count = 1
        for k in range(1, N):
            if temp_board[k][col] == temp_board[k-1][col]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1

    return max_count

for i in range(N):
    for j in range(N):
        
        temp_board = deepcopy(board)

        if i + 1 < N and board[i][j] != board[i+1][j]:
            temp_board = deepcopy(board)
            temp_board[i][j], temp_board[i+1][j] = temp_board[i+1][j], temp_board[i][j]
            answer.append(check_max_count(temp_board))
        
        if j + 1 < N and board[i][j] != board[i][j+1]:
            temp_board = deepcopy(board)
            temp_board[i][j], temp_board[i][j+1] = temp_board[i][j+1], temp_board[i][j]
            answer.append(check_max_count(temp_board))


print(max(answer))