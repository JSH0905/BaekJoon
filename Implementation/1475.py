# 방 번호

import sys

N = str(sys.stdin.readline().strip())

number_count = [0] * 10

for i in N:
    if i == "6" or i == "9":
        if number_count[6] <= number_count[9]:
            number_count[6] += 1
        else:
            number_count[9] += 1
    else:
        number_count[int(i)] += 1

print(max(number_count))
