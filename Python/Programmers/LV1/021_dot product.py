# 내적

def solution(a, b):
    answer = 1234567890

    nl = len(a)
    temp = 0
    for i in range(nl):
        temp += a[i] * b[i]

    answer = temp

    return answer