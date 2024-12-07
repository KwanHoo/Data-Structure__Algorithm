# 정수 제곱근 판별

def solution(n):
    answer = 0

    ## 거듭제곱 연산자 **
    sqrt = n ** (1 / 2)  ## 루트씌우는거
    print(sqrt)  # 1.7320508075688772  	11.0
    print(sqrt % 1)  # 0.7320508075688772      0.0
    if (sqrt % 1 == 0):  ## 나머지가 0 -> 소수점 숫자 판별
        answer = (sqrt + 1) ** 2
    else:
        answer = -1

    return answer