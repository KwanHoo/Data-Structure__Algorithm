# 예산

#! 물품을 구매해 줄 때는 각 부서가 신청한 금액만큼을 모두 지원
def solution(d, budget):
    answer = 0 # 가능한 부서의 수
    for i in sorted(d):
        budget -= i
        if budget < 0:
            break
        answer += 1
    return answer