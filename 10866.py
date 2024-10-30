#덱(deque)

## Deque(덱)이란? : 양방향 큐

### push_front X: 정수 X를 덱의 앞에 넣는다.
### push_back X: 정수 X를 덱의 뒤에 넣는다.
### pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
### pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
### size: 덱에 들어있는 정수의 개수를 출력한다.
### empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
### front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
### back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
from collections import deque

def push_front(deq, X):
    deq.appendleft(X)

def push_back(deq, X):
    deq.append(X)

def pop_front(deq):

    if len(deq) == 0:
        print(-1)
    else:
        front_num = deq.popleft()
        print(front_num)

def pop_back(deq):

    if len(deq) == 0:
        print(-1)
    else:
        back_num = deq.pop()
        print(back_num)

def size(deq):
    print(len(deq))

def empty(deq):
    if len(deq) == 0:
        print(1)
    else:
        print(0)

def front(deq):
    if len(deq) == 0:
        print(-1)
    else:
        print(deq[0])

def back(deq):
    if len(deq) == 0:
        print(-1)
    else:
        print(deq[-1])


deq = deque()

N = int(sys.stdin.readline())

for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        push_front(deq, int(command[1]))

    elif command[0] == 'push_back':
        push_back(deq, int(command[1]))

    elif command[0] == 'pop_front':
        pop_front(deq)

    elif command[0] == 'pop_back':
        pop_back(deq)

    elif command[0] == 'size':
        size(deq)

    elif command[0] == 'empty':
        empty(deq)

    elif command[0] == 'front':
        front(deq)

    elif command[0] == 'back':
        back(deq)

    else:
         print("예외 발생")
