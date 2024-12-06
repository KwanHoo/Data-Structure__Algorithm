# 프로그래머스 LV1 짝수와 홀수

def solution(num):
    if num % 2 == 0:
        # 짝
        answer = "Even"
    else:
        # 홀
        answer = "Odd"
    return answer