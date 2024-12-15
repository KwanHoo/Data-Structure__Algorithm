# 구명보트

# 그리디
# 조건 : 최대 2명, 한번에 100kg 이하
# sol) 제일 무거운사람 + 제일 가벼운 사람

def solution(people, limit):
    answer = 0
    people.sort()
    # 정렬 후 몸무게 큰 사람과 작은사람 짝지어야 많이 태울 수 있을 것 같음

    start = 0
    end = len(people) - 1

    while (start <= end):  # 두 명씩 구출해서 다 구출할 때까지 비교
        if (people[start] + people[end] <= limit):  # limit 보다 작거나 같으면 둘다 구출 가능
            start += 1
            end -= 1
        else:  # 안되면 일단 몸무게 큰 사람부터 먼저 구출
            end -= 1
        answer += 1
    return answer


## 22점 -> 정 14.8, 효 7.4
## -> 작은 거부터 2명씩 보트 묶는 코드임 -> 그리디 아님 ㅌ
def solution2(people, limit):
    answer = 0
    count = 0
    people.sort(reverse=True)
    # print(people)
    templ = []
    for i in range(len(people)):
        temp = people.pop()
        # print(temp, people)

        templ.append(temp)
        a = sum(templ)

        if a > limit and temp > limit / 2:
            count += 2
            templ = []
        elif a == limit:
            count += 1
            templ = []
        elif a > (limit / 2):
            count += 1
            templ = []

    # print(templ)
    answer = count

    return answer