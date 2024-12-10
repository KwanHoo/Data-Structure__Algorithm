# 음양 더하기

def solution(absolutes, signs):
    answer, temp = 0,0
    for i in range(len(signs)):
        if signs[i]:
            temp += absolutes[i]
        else:
            temp -= absolutes[i]
    answer = temp
    return answer