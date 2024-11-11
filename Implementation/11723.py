# 집합

## 리스트로 풀기에는 메모리가 부족함
### 해결방법 : set 사용

import sys

S = set()

M = int(sys.stdin.readline())
for i in range(M):
    operationAndValue = sys.stdin.readline().split()

    if len(operationAndValue) == 1:

        if operationAndValue[0] == "all":
            S = set([i for i in range(1,21)])

        elif operationAndValue[0] == "empty":
            S.clear()

        else:
            exit()

    else:
        operation, value = operationAndValue[0], int(operationAndValue[1])

        if operation == "add":
            S.add(value)

        elif operation == "remove":
            S.discard(value)

        elif operation == "toggle":
            if value in S:
                S.remove(value)
            else:
                S.add(value)

        elif operation == "check":
            if value in S:
                print(1)
            else:
                print(0)
        else:
            exit()