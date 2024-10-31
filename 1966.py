# 프린터 큐

## 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
## 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

import sys

def checkPriority(list, curios_loc_of_doc):

    removed_order = 1
    while len(list) > 1:
        if list[0] < max(list):
            list.append(list.pop(0))

        else:
            if curios_loc_of_doc == 0 : break

            list.pop(0)
            removed_order += 1

        curios_loc_of_doc = curios_loc_of_doc - 1 if curios_loc_of_doc > 0 else len(list) - 1

    print(removed_order)

count_of_testCase = int(sys.stdin.readline()) ## 테스트 케이스의 수

for _ in range(count_of_testCase):

    count_of_docs, curios_loc_of_doc = map(int, sys.stdin.readline().split()) ### 문서의 개수, 궁금한 문서의 위치
    priority = list(map(int, sys.stdin.readline().split()))

    checkPriority(priority, curios_loc_of_doc)

