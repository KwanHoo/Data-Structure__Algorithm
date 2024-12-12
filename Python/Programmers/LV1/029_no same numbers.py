# 같은 숫자는 싫어

from collections import deque


def solution(arr):
    answer = []
    queue = deque()  # 큐 구현
    queue.append(arr[0])
    print(queue)
    for i in range(1, len(arr)):
        temp = arr[i]

        comp = queue[-1]
        # print(comp, temp)
        # 해당 원소가 있으면 넘기고 없으면 반영
        if comp == temp:
            continue
        else:
            queue.append(temp)

    answer = list(queue)
    return answer