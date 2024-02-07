# 알고리즘 고득점 KIT _ 스택/큐
# 같은 숫자는 싫어

# 연속적으로 나타나는 숫자는 하나만 남기고 제거
# 순서는 유지 : 큐

from collections import deque

## 입력으로 숫자 배열 들어옴
arr = list(map(int,input().split()))

def solution(arr):
    answer = []
    queue = deque()     #큐 구현
    queue.append(arr[0])
    for i in range(1,len(arr)):
        temp = arr[i]
        comp = queue[-1]

        # 해당 원소가 있으면 넘기고 없으면 반영
        if comp == temp:
            continue
        else:
            queue.append(temp)

    answer = list(queue)
    return answer

solution(arr)

## 24.02.07 : 2m
