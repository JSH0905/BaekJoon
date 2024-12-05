# 수 이어 쓰기1

# 처음에 푼 방법 => 시간 초과

    # N = int(sys.stdin.readline())

    # num = ''
    # for i in range(1, N+1):
    #     num += str(i)

    # print(len(num))


import sys

N = int(sys.stdin.readline())

length = 0
digit = 1
start = 1

while start <= N:
    end = min(N, 10**digit - 1)  
    length += (end - start + 1) * digit
    start *= 10
    digit += 1

print(length)
