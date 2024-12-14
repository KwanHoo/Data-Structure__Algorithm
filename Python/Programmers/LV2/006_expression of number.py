# 숫자의 표현

def solution(n):
    answer = 0

    for i in range(1, n + 1):
        sum_val = 0
        for j in range(i, n + 1):
            sum_val += j
            ## n 값인경우 answer +1
            if sum_val == n:
                answer += 1
            ## 더하다가 sum값 n보다 크면 break
            elif sum_val > n:
                break

    return answer
