### 분수 찾기

# 1/1
# -> 1/2 -> 2/1
# -> 3/1 -> 2/2 -> 1/3
# -> 1/4 -> 2/3 -> 3/2 -> 4/1
# -> 5/1 -> 4/2 -> 3/3 -> 2/4 -> 1/5

# X번째 분모는??

## 홀수 라인 : 분모 증가 / 짝수 라인 : 분자 증가

## 풀이
import sys

X = int(sys.stdin.readline())

line = 0
end_num_of_line = 0

while end_num_of_line < X:
    line += 1
    end_num_of_line += line

diff = end_num_of_line - X

if line % 2 == 0:
    numerator = line - diff
    denominator = diff + 1
else:
    numerator = diff + 1
    denominator = line - diff

print(f'{numerator}/{denominator}')






