# 프로그래머스 LV1 약수의 합

def solution(n):
    answer = 0
    # 약수 리스트 생성
    nlist = [1]

    for i in range(2, n + 1):
        if n % i == 0:
            nlist.append(i)
    # 합
    answer = sum(nlist)
    return answer