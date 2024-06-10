# 알고리즘 고득점 KIT _ 힙
# 더 맵게

## 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 함!!

import heapq
def solution1(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville)>1:
        min1 = heapq.heappop(scoville)
        if min1 < K:
            min2 = heapq.heappop(scoville)
            new = min1 + (min2 * 2)
            answer += 1
            heapq.heappush(scoville, new)
        else:
            break

    # print(scoville)

    return -1 if scoville[0] < K else answer



def solution(scoville, K):
    count = 0  # 반환 할 결과값, 섞은 횟수
    heapq.heapify(scoville)  # 스코빌 지수 우선순위 큐

    # 스코빌 지수가 1개 남을 때까지 while loop
    while len(scoville) > 1:
        # '가장 맵지 않은 음식의 스코빌 지수'
        first = heapq.heappop(scoville)

        # '가장 맵지 않은 음식의 스코빌 지수'가 K보다 작다면
        if first < K:
            count += 1  # 섞은 횟수 1씩 증가
            second = heapq.heappop(scoville)  # '두 번째로 맵지 않은 음식의 스코빌 지수'
            heapq.heappush(scoville, (first + (second * 2)))  # '특별한 방법으로 섞기' 후 다시 담기
        # 가장 맵지 않은 음식의 스코빌 지수'가 K 이상이면 종료
        else:
            break

    # '가장 맵지 않은 음식의 스코빌 지수'가 K보다 작으면 -1, 그렇지 않으면 while loop 섞은 횟수 반환
    return -1 if scoville[0] < K else count

scoville = [1, 2, 3, 9, 10, 12]
K = 7

result = solution1(scoville, K)