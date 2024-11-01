# 통계학

import sys
from collections import Counter

def get_arithmetic_mean(numbers):
    print(round(sum(numbers) / len(numbers)))

def get_median(numbers):
    numbers.sort()
    print(numbers[len(numbers)//2])

def get_mode(numbers):

    count = Counter(numbers)
    max_freq = max(count.values())
    modes = [k for k, v in count.items() if v == max_freq]

    if len(modes) == 1:
        print(modes[0])
    else:
        modes.sort()
        print(modes[1])

def get_range(numbers):
    print(max(numbers) - min(numbers))


cnt_of_num = int(sys.stdin.readline())

numbers = []

for _ in range(cnt_of_num):
    numbers.append(int(sys.stdin.readline()))

get_arithmetic_mean(numbers)
get_median(numbers)
get_mode(numbers)
get_range(numbers)