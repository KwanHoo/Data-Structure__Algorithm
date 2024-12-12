# 폰켓몬

def solution(nums):
    answer = 0

    snum = set(nums) ## 중복제거
    # print(snum)
    nl = len(nums)/2
    sl = len(snum)
    # print(nl, sl)
    if sl < nl: ## sl(중복제거)이 작은 경우 -> sl return
        answer = sl
    else: ## nl(절반나눈수)이 작거나 같은 경우
        answer = nl
    return answer