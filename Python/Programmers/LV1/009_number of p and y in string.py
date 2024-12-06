# 문자열 내 p와 y의 개수

def solution(s):
    answer = False
    pcount = 0
    ycount = 0
    for i in s:
        if i == 'p' or i == 'P':
            pcount += 1
        elif i == 'y' or i == 'Y':
            ycount += 1

    if pcount == ycount:
        answer = True

    return answer