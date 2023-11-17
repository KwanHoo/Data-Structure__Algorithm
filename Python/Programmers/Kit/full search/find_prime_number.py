# 알고리즘 고득점 KIT _ 완전탐색
# 소수 찾기

# 소수 : 1보다 큰 자연수 중 1과 자기 자시만을 약수로 가지는 수

# 순열 조합 이용!!
from itertools import permutations

numbers = str(input())

def solution(numbers):
    answer = []
    nums = [n for n in numbers]                     # numbers를 하나씩 자른 것
    per = []

    ## 순열 조합
    for i in range(1, len(numbers)+1):              # numbers의 각 숫자들을 순열로 모든 경우 만들기
        per += list(permutations(nums, i))          # i개씩 순열조합

    ## .join 이용 하나의 숫자로 만듬
    new_nums = [int(("").join(p)) for p in per]     # 각 순열조합을 하나의 int형 숫자로 변환
    # print(new_nums)
    # print(per)

    ## 소수 판별 (에라토스테네스의 체)
    for n in new_nums:                              # 모든 int형 숫자에 대해 소수인지 판별
        if n < 2:                                   # 2보다 작은 1,0의 경우 소수아님
            continue
        check = True
        for i in range(2, int(n**0.5) +1):          # n의 제고급 보다 작은 숫자까지만 나눗셈
            if n%i ==0:                             # 하나라도 나눠떨어진다면 소수 아님!
                check = False
                break
        if check:
            answer.append(n)                        # 소수일경우 answer 배열에 추가

    return len(set(answer))                         # set을 통해 중복 제거 후 반영

solution(numbers)