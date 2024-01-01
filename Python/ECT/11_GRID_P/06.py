# 06 무지의 먹방 라이브

# 회전판에 N개의 음식
# 1초동안 섭취한 후 남은 음식은 그대로 두고 다음음식 섭취 (가장 가까운 번호 다음음식)

## 네트워크 장애가 발생후 몇번 음식부터 다시 섭취하면 되는지 return
import heapq

## 풀이 참고
def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0       # 먹기 위해 사용한 시간
    previous = 0        # 직전에 다 먹은 음식 시간

    length = len(food_times)    # 남은 음식의 개수

    # sum_value + (현재의 음식시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1         # 다 먹은 음식 제외
        previous = now      # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번재 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1])      # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]

## 초기 접근
def solution2(food_times, k):
    if sum(food_times) <=k:
        return -1

    answer = 0
    breakp = True
    i = 0 # 리스트 순환번호
    time = 0 # 시간
    # print(food_times)
    while breakp:
        # print(i)
        temp = food_times[i]

        # 마지막인경우
        if i == len(food_times)-1:
            if temp == 0:
                i = 0
                continue
            else:
                temp -= 1
                food_times[i] = temp
                time += 1
                i = 0
        # 마지막 아닌경우
        else:
            if temp == 0:
                i += 1
                continue
            else:
                temp -= 1
                food_times[i] = temp
                time += 1
                i += 1

        if k == time:
            breakp = False
            answer = i+1

    return answer

food = [3, 1, 2]

result = solution(food, 5)

print(result)

# 24.01.01 25m 정확성: 28.1/100, 효율성 0