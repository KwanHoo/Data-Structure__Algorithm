# 콜라츠 추측

def solution(num):
    answer = 0
    temp = 0
    c = 0
    while((num != 1) and (c < 500)) :
        if (num % 2 == 0 ):
            # even
            temp = num / 2
        else:
            # odd
            temp = num * 3 + 1
        num = temp
        c +=1
    if c == 500:
        answer = -1
    else:
        answer = c
    return answer