# 부족한 금액 계산하기

def solution(price, money, count):
    answer = -1

    suml = []

    for i in range(1, count + 1):
        temp = i * price

        suml.append(temp)
    lists = sum(suml)

    temp = lists - money ## 부족한 차액금액

    ## 금액 부족한 경우 부족한 금액값 리턴
    if temp > 0:
        answer = temp
    else: ## 금액 부족하지 않은 경우 0리턴
        return 0

    return answer