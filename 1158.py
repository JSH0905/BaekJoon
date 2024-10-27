### 요세푸스 문제

### 입력 : N, K

### N=7, K=3 -> 1,  4,의 사람이 존재하고 3번째 사람마다 제거
### -> 3,6,2,7,5,1,4

### 풀이 = 큐를 이용.
### 큐의 구현 => 3가지 메서드 정의 : Enqueue / Dequeue / peek
### 구현 방식 => 크게 두가지 : 배열 OR 링크드 리스트
### 이 문제에서 N으로 인해 큐의 크기가 고정이기 때문에 배열을 이용하도록 하겠음.

import sys

circular_queue = []
josephus_permutation = []
pointer = 0

N, K = map(int, sys.stdin.readline().split())

for i in range(1, N+1):
    circular_queue.append(i) ### 1 ~ N번의 사람들을 원형 테이블에 앉힘.

for k in range(N):

    pointer += K - 1

    if pointer >= len(circular_queue):
        pointer = pointer % len(circular_queue)

    josephus_permutation.append(str(circular_queue.pop(pointer)))

print("<",", ".join(josephus_permutation)[:],">", sep='')






