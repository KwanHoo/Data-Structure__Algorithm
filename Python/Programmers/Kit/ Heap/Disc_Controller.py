# 알고리즘 고득점 KIT _ 힙
# 디스크 컨트롤러

## 고려
# 1) 현재 시점에서 처리할 수 있는 작업인지를 판별하는 조건은
#       작업의 요청 시간이 바로 이전에 완료한 작업의 시작 시간(start)보다 크고
#       현재 시점(now)보다 작거나 같아야 한다.
# 2) 동시에 실행할 수 있는 작업중 처리시간이 적은 작업을 먼저 처리

import heapq

def solution(jobs):
    answer = 0
    start = -1  # 마지막 완료시간
    now = 0     # 현재시간
    i = 0       # 처리개수
    heap = []

    ## [작업의 소요시간, 작업이 요청되는 시점]
    ## heap 배열 재세팅
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])

        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1]) # 요청으로부터 처리시간
            i += 1
        else:
            now += 1
    return answer // len(jobs)

## [작업이 요청되는 시점, 작업의 소요시간]
jobs = [[0, 3], [1, 9], [2, 6]]

result = solution(jobs)

print(result)  # 9