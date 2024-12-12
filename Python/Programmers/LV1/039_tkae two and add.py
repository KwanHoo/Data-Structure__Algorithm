# 두개 뽑아서 더하기

# 조합이용
from itertools import combinations


def solution1(numbers):
    answer = set() ## 중복제거로 집합선언
    for i in list(combinations(numbers, 2)):
        print(i)
        answer.add(sum(i))
    return sorted(answer)


def solution2(numbers):
    answer = []

    clist = list(combinations(numbers, 2)) ## 조합 리스트 추출

    # print(clist)

    for i in range(len(clist)):
        temp = sum(list(clist[i]))
        answer.append(temp)
    # print(answer)
    temp2 = set(answer) ## 중복제거
    # print(temp2)
    answer = list(temp2)
    return answer