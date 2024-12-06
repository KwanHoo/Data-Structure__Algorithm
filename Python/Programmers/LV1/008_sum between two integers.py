# 두 정수 사이의 합

def solution(a, b):
    answer = 0

    big, sml, temp = 0, 0, 0
    if a > b:
        big, sml = a, b
    else:
        big, sml = b, a
    for i in range(sml, big + 1):
        temp += i
    answer = temp
    return answer